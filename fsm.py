from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '早安'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '午安'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '晚安'
    
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == '吃飯阿'

    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == '掰掰'

    def on_enter_state1(self, update):
        update.message.reply_text("早安")
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("午安")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("晚安")
        #self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')

    def on_enter_state4(self, update):
        update.message.reply_text("不要")
        #self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')

    def on_enter_state5(self, update):
        update.message.reply_text("掰掰")
        self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state5')
