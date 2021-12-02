from tkinter import *
from anime_chatbot import *
from softwareengineeringproject import *

bot_name = "MyAnimeBot"
bot_response = "Here should be the answer"

# Colors
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

# Font
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg = BG_COLOR, fg = TEXT_COLOR, text = "MyAnimeBot", font = FONT_BOLD, pady = 10)
        head_label.place(relwidth = 1)

        # tiny divider
        line = Label(self.window, width = 450, bg = BG_GRAY)
        line.place(relwidth = 1, rely = 0.07, relheight = 0.012)

        # text widget
        self.text_widget = Text(self.window, width = 20, height = 2, bg = BG_COLOR, fg = TEXT_COLOR, font = FONT, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor = "arrow", state = DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight = 1, relx = 0.975)
        scrollbar.configure(command = self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg = BG_GRAY, height = 80)
        bottom_label.place(relwidth = 1, rely = 0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg = "#2C3E50", fg = TEXT_COLOR, font = FONT)
        self.msg_entry.place(relwidth = 0.74, relheight = 0.06, rely = 0.008, relx = 0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text = "Send", font = FONT_BOLD, width = 20, bg = BG_GRAY, command = lambda: self._on_enter_pressed(None))
        send_button.place(relx = 0.77, rely = 0.008, relheight = 0.06, relwidth = 0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        # deletes text from input box when sending message
        self.msg_entry.delete(0, END)

        # displays sender's message in the message box
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state = DISABLED)

        # detects the language in which the message was sent
        lang = detect_language(msg)
        msg_trans = translate_input(msg, lang)

        #displays the chatbot's response in the message box
        output = Anime_Bot.get_response(msg_trans)
        output_trans = translate_output(output, lang) # translate the message in the langauge that the initial message was sent
        msg2 = f"{bot_name}: {output_trans}\n\n"  # get_response is the function that returns the chatbot's answer to msg input
        self.text_widget.configure(state = NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state = DISABLED)

        self.text_widget.see(END) # scrolls to the end so you can see last message
