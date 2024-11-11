import re

class SyntaxChecker:
    def __init__(self):
        self.error_messages = {
            'missing_semicolon': 'Missing semicolon at the end of the line.',
            'unmatched_brackets': 'Unmatched brackets detected.',
            'indentation_error': 'Incorrect indentation.',
        }

    def check_syntax(self, code):
        errors = []

        # Check for missing semicolons (Python-specific)
        lines = code.split('\n')
        for line_num, line in enumerate(lines, start=1):
            if re.match(r'^[^\s#].*[^:]$', line) and not line.strip().endswith(':') and not line.strip().endswith(';'):
                errors.append((line_num, self.error_messages['missing_semicolon']))

        # Check for unmatched brackets
        if not self.check_brackets(code):
            errors.append((line_num, self.error_messages['unmatched_brackets']))

        # Check for indentation errors (basic check)
        for line_num, line in enumerate(lines, start=1):
            if line.startswith(' ') and (len(line) - len(line.lstrip())) % 4 != 0:
                errors.append((line_num, self.error_messages['indentation_error']))
                
        return errors

    def check_brackets(self, code):
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        for char in code:
            if char in brackets.keys():
                stack.append(brackets[char])
            elif char in brackets.values():
                if not stack or char != stack.pop():
                    return False
        return not stack
