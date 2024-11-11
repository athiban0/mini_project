class ThemeManager:
    def __init__(self):
        self.themes = {
            'dark': {
                'bg': '#1e1e1e',
                'fg': '#c7c7c7',
                'highlight': '#ffaa00'
            },
            'light': {
                'bg': '#ffffff',
                'fg': '#000000',
                'highlight': '#ff4500'
            },
            'anime': {
                'bg': '#282a36',
                'fg': '#f8f8f2',
                'highlight': '#ff79c6',
                'icon': 'assets/anime_icons/tanjiro.png'
            }
        }

    def get_theme(self, theme_name):
        return self.themes.get(theme_name, self.themes['dark'])
