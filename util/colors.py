purple = "\033[0;35m"
green = "\033[0;32m"
red = "\033[0;31m"
end = "\033[0m"
cyan = "\033[0;36m"
gray = "\033[0;37m"


def mkcolor(color=end):
    def styleize_text(text):
        return "{}{}{}".format(color, text, end)

    return styleize_text


purple_wrapper = mkcolor(purple)
green_wrapper = mkcolor(green)
red_wrapper = mkcolor(red)
cyan_wrapper = mkcolor(cyan)
gray_wrapper = mkcolor(gray)
