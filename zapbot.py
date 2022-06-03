from selenium import webdriver
import time

class WhatsappBot:
    def _init_(self):
        self.mensagem = "teste"
        self.grupos = ["Família da hora", "Grupo provisório Família"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_patch=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        #<span dir="auto" title="Família da hora" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr"><span class="matched-text i0jNr">Família</span> da hora</span>
        #<div tabindex="-1" class="p3_M1">
        #<span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(30)
        for grupos in self.grupos:
            grupos = self.driver.find_element_by_xpath(f"//span[@title='{grupos}']")
            time.sleep(3)
            grupos.click()
            chat_box = self.driver.find_elemet_by_class_name('p3_M1')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpatch("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)


bot = WhatsappBot()
bot.EnviarMensagens()