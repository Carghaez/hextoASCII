import sublime
import sublime_plugin


class DecToHexCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
        for j in range(0, len(reglist)):
            hx = v.substr(v.sel()[j])
            hx = hex(int(hx, 10))
            v.replace(edit, v.sel()[j], hx)
