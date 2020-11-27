import urwid
from urwid import main_loop

blank = urwid.Divider()

class SimpleInterface(urwid.Frame):
    
    storyCache = urwid.SimpleListWalker([])
    storyPanel = urwid.ListBox(storyCache)
    inputField = urwid.Edit(u"> ",)
    storyWidgets = urwid.Frame(storyPanel, blank, inputField)
    storyFrame = urwid.LineBox(storyWidgets,  u"Title")
    
    def __init__(self, app) -> None:
        self.__app = app
        super().__init__(self.storyFrame)
        self.update_storyTitle(self.app.session.scene.name)
    
    def _get__app(self) -> object:
        return self.__app
    app = property(_get__app)
    
    def update_storyTitle(self, newTitle: str):
        self.storyFrame.set_title(newTitle)
    def update_storyPanel(self, text: str):
        while len(self.storyCache) > 40:
            self.storyCache.pop(0)
        self.storyCache.append(urwid.Text(text))
        self.storyCache.append(blank)
    def focus_lastStoryEntry(self) -> None:
        self.storyPanel.set_focus(len(self.storyCache)-1)
    
    def keypress(self, size, key):
        unhandled = self.key_events(key)
        if not unhandled:
            pass
        else:
            super().keypress(size, key)
    def key_events(self, key):
        try:
            if key == ' ' and self.storyWidgets.focus_part != 'footer':
                self.storyWidgets.set_focus('footer')
            elif key == 'enter' and self.storyWidgets.focus_part == 'footer':
                request = self.inputField.edit_text
                self.inputField.edit_text = ''
                self.app.handle_userInput(request)
                self.storyWidgets.set_focus('body')
            elif key == 'esc':
                raise urwid.ExitMainLoop()
            elif key in ['n', 's', 'w', 'e', 'u', 'd'] and self.storyWidgets.focus_part == 'body':
                self.__app.move_player(key)
            elif key == 'l' and self.storyWidgets.focus_part == 'body':
                self.app.look_around()
            else:
                return key
        except AssertionError as msg:
            self.update_storyPanel(u"{}".format(msg))
        
        return False
