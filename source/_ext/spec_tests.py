import os
import json
from docutils import nodes

def spec_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    parts = text.split('|', 1)
    if len(parts) != 2:
        msg = inliner.reporter.error(
            'Spec role must have "id|text" format', line=lineno)
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]
    spec_id = parts[0].strip()
    text_content = parts[1].strip()

    outer = nodes.inline(classes=['spec-nowrap'])
    assertion = nodes.inline(classes=['spec-assertion'])

    # Текст утверждения
    parsed_nodes, messages = inliner.parse(text_content, lineno, inliner, inliner.parent)
    assertion.extend(parsed_nodes)
    assertion += messages

    # Звёздочка (переключатель)
    toggle_star = nodes.inline(text='*', classes=['spec-id-toggle'])

    # Скрытый ID
    id_node = nodes.inline(text=f'[{spec_id}]', classes=['spec-id', 'spec-id-hidden'])

    assertion += toggle_star
    assertion += id_node
    outer += assertion

    env = inliner.document.settings.env
    if not hasattr(env, 'spec_tests_map'):
        env.spec_tests_map = {}
    env.spec_tests_map[spec_id] = [spec_id]

    return [outer], []

# ---------- Вспомогательная функция ----------
def add_grouped_inline(container, text, classify_func):
    """
    Разбивает text на последовательности символов одного класса
    и добавляет в container узлы: span с классом или простой текст (если класс None).
    classify_func(char) -> class_name или None (оставить без обёртки).
    """
    if not text:
        return
    i = 0
    n = len(text)
    while i < n:
        current_class = classify_func(text[i])
        j = i + 1
        while j < n and classify_func(text[j]) == current_class:
            j += 1
        segment = text[i:j]
        if current_class is None:
            # Текстовый узел без обёртки
            container.append(nodes.Text(segment))
        else:
            container.append(nodes.inline(text=segment, classes=[current_class]))
        i = j

# ---------- Классификаторы ----------
def uc_classify(ch):
    if ch.isdigit() or ch == '+':
        return 'fake-smallcaps'
    elif ch.isalpha():  # A-F, U
        return 'uc-code'
    else:
        # пробелы, скобки и прочее – без обёртки (можно оставить None)
        return None

def scmp_classify(ch):
    if ch.isalpha():
        return 'scmp'
    elif ch.isdigit() or ch in ('+', '-', '.', ','):  # знаки, цифры
        return 'fake-smallcaps'
    else:
        return None  # пробелы и прочее

# ---------- Роль uc ----------
def uc_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    parts = text.split('|', 1)  # делим по первому пробелу: код и символ
    if len(parts) != 2:
        msg = inliner.reporter.error(
            'uc role requires "code symbol" format, e.g. 005F _', line=lineno)
        return [inliner.problematic(rawtext, rawtext, msg)], [msg]

    code = parts[0].strip()
    char = parts[1].strip()

    wrapper = nodes.inline(classes=['uc'])

    # Разбираем строку "U+<code>" целиком, группируя символы
    full_code_str = 'u+' + code
    add_grouped_inline(wrapper, full_code_str, uc_classify)

    # Пробел
    wrapper += nodes.inline(text=' ')
    # Символ в скобках
    wrapper += nodes.inline(text=f'({char})', classes=['uc-char'])

    return [wrapper], []

# ---------- Роль scmp ----------
def scmp_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    wrapper = nodes.inline(classes=['scmp-wrapper'])   # обёртка не обязательна
    add_grouped_inline(wrapper, text, scmp_classify)
    return [wrapper], []

# ---------- Сохранение JSON (без изменений) ----------
def on_build_finished(app, exception):
    if exception is not None:
        return
    if hasattr(app.env, 'spec_tests_map') and app.env.spec_tests_map:
        json_path = os.path.join(app.outdir, '..', 'spec_tests_map.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(app.env.spec_tests_map, f, ensure_ascii=False, indent=2)

# ---------- Регистрация всех ролей ----------
def setup(app):
    app.add_role('spec', spec_role)
    app.add_role('uc', uc_role)
    app.add_role('scmp', scmp_role)
    app.connect('build-finished', on_build_finished)
    return {
        'version': '1.1',
        'parallel_read_safe': True,
    }