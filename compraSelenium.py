# minhas importações
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


class Test_Selenium_Webdriver():

 # Início
    def setup_method(self, method):

        self.driver = webdriver.Chrome(
            'C:\\Users\\Juliana.bueno\\Desktop\\CompraCursoSelenium\\drivers\\chromedriver102.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def teardown_method(self):
        self.driver.quit()

    # Definição do Teste
    @pytest.mark.parametrize('id, termo, curso, preco', [
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
    ])
    def testar_comprar_curso_com_click_na_lupa(self, id, termo, curso, preco):

        # O Selenium abre a url indicada - site alvo do teste
        self.driver.get('https://www.iterasys.com.br')
        self.driver.find_element(By.ID, 'searchtext').click()
        self.driver.find_element(By.ID, 'searchtext').clear()
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):

        self.driver.get('https://www.iterasys.com.br')
        # O Selenium clica na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').click()
        # O Selenium apaga o conteúdo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # O Selenium escreve 'mantis' na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # O Selenium pressiona a tecla Enter
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # O Selenium clica em 'Matricule-se'
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Selenium valida o nome do curso no carrinho de compras
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        # O Selenium valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

    # Fim do programa
        self.driver.close()