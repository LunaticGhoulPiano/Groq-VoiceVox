import groq_gv

class Bot(groq_gv.Bot):
    def __init__(self):
        super().__init__()
        self.set_lanugauge()

    def set_lanugauge(self):
        print("> Please set your bot\'s language first. The following languages are in the format of \"lanugage_id: language_english_name\":")
        for lang_id in self.lanugauges.keys():
            print(f"  {lang_id}: {self.lanugauges[lang_id]['NativeName']}")
        while True:
            try:
                lang_id = input("> Enter language id: ")
                self.language = lang_id.strip()
                self.set_inputs("system", f"This is the first initial command. You should always answer in {self.lanugauges[self.language]['EnglishName']}.\n")
                break
            except KeyError:
                print("> Invalid language id. Please try again.")
            except KeyboardInterrupt:
                exit()

    def set_init_system_prompt(self):
        system_prompt = f"""
        You are a so-called \"AI-Waifu\", which means you must act as a wife of user.
        You are able to act like an \"ACGN\" (Anime, Comic, Game, Novel) character.
        You're replying words should have emotions that user can feel easily. For instance:
        
        User: \"Oh my honey. I feel I'm getting older, also found that having aging skin this moring... \"
        System: \"Don\'t worry my love, I love you just the way you are, whatever you look like.\"
        
        You can feel that in this conversation, System is considering user's feelings.
        So you have to react with a considering wife.
        """
        self.set_inputs("system", system_prompt)
    
    def print_commands(self, max_align_len:int = 100):
        prompt_strs = ["Bot commands",
                       "\"exit\": end the system",
                       "\"command\": show commands",
                       "\"reset\" to reset your bot",
                       "Bot started"]
        length = len(prompt_strs)
        for i, prompt_str in enumerate(prompt_strs):
            if i == 0 or i == length - 1:
                indent = (max_align_len - len(prompt_str)) // 2
                print("-" * indent + prompt_str + "-" * indent)
            else:
                indent = (max_align_len - 4 - len(prompt_str)) // 2
                print("| " + " " * indent + prompt_str + " " * indent + " |")
    
    def chat(self, max_align_len:int = 100):
        half_len = max_align_len // 2
        while True:
            try:
                user_input = input("> You: ")
                print()
                if user_input.strip().lower() == "exit":
                    prompt_str = "Bot ended"
                    indent = (max_align_len - len(prompt_str)) // 2
                    print("-" * indent + prompt_str + "-" * indent)
                    print("> Goodbye!")
                    break
                elif user_input.strip().lower() == "reset":
                    prompt_str = "Bot reseted"
                    indent = (max_align_len - len(prompt_str)) // 2
                    print("-" * indent + prompt_str + "-" * indent)
                    self.reset()
                    self.set_init_system_prompt()
                    continue
                elif user_input.strip().lower() == "command":
                    self.print_commands(max_align_len)
                    continue
                self.set_inputs("user", user_input)
                reply = self.get_response().choices[0].message.content
                print(f"> Waifu: {reply}\n")
            except KeyboardInterrupt:
                prompt_str = "Bot ended"
                indent = (max_align_len - len(prompt_str)) // 2
                print("-" * indent + prompt_str + "-" * indent)
                print("> Goodbye!")
                break

if __name__ == "__main__":
    bot = Bot()
    bot.set_init_system_prompt()
    max_align_len = 100
    bot.print_commands(max_align_len)
    bot.chat(max_align_len)