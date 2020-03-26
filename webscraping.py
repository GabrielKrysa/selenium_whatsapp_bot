from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

url = "https://web.whatsapp.com/"

#carregando o executavel do navegador firefox
binary = FirefoxBinary("#caminho do executavel do navegador firefox")

#carregando o driver do navegador firefox
driver = webdriver.Firefox(
    firefox_binary=binary, executable_path=r"#caminho do driver do navegador firefox GeckoDriver")

#abre o navegador
driver.get(url)

#tempo para autenticação do whatsapp com leitura do QRCode
time.sleep(10)  

# Lista de contatos para enviar mensagem
list_search = []

for name_search in list_search:

    #campo de busca de contatos
    search_field = driver.find_element_by_xpath(
    "//div[@class='_3u328 copyable-text selectable-text']")

    time.sleep(0.5)
    
    #insere o nome do contato no campo de busca
    search_field.send_keys(name_search)
    
    time.sleep(5)
    
    #entra no primeiro contato correspondente da busca
    driver.find_element_by_xpath("//div[@class='X7YrQ']").click()
    time.sleep(0.5)
    
    #none que esta salvo do cantato
    name = driver.find_element_by_xpath(
        "//span[@class='_19RFN _1ovWX _F7Vk']").text

    #status de visto por ultimo ou online
    current_status = driver.find_element_by_xpath(
        "//span[@class='_315-i _F7Vk']").text

    #clica no input de mensagem
    driver.find_element_by_xpath("//div[@class='_13mgZ']").click()
    
    #resgata o input de mensagem
    message = driver.find_element_by_xpath(
        "//footer[@class='_1N6pS']//div//div//div/div[@class='_3u328 copyable-text selectable-text']")
    
    #escreve a mensagem no input
    message.send_keys(
        "Olá "+name_search+", mensagem enviado automaticamente!")

    #envia a mensagem
    driver.find_element_by_xpath("//button[@class='_1XCAr']").click()
    
    #limpa o campo de busca
    driver.find_element_by_xpath("//footer[@class='_1N6pS']//div//div//button[@class='_3M-N-']").click()

#fecha o navegador
driver.quit()