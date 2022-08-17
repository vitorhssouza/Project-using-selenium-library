from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
from modulos.funcoes import *
from time import sleep



class Empresa:

    def __init__(self, codigo: list) -> list:
        self.__codigo = codigo

    @property
    def codigo(self: object) -> list:
        return self.__codigo


class B3:

    def __init__(self: object, site: str) -> None:
        self.__site = site

    @property
    def site(self: object) -> str:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.get(self.__site)
        driver = input('Nesse site encontramos codígos de ações que estão na bolsa de valores\n'
                       'Aperte ENTER para fechar o site.')
        self.__b3 = driver
        return self.__site


class Uol(Empresa):

    def __init__(self: object, codigo: list, uol: str) -> None:
        super().__init__(codigo)
        self.__uol = uol

    @property
    def uol(self: object) -> None:
        options = Options()
        options.add_argument('--headless')

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

        driver.get(self.__uol)

        valores = list()
        data_hora = list()
        codigos_empresas = list()

        for empresa in self._Empresa__codigo:
            if empresa not in '':

                input_busca = driver.find_element(By.ID, 'filled-normal')

                input_busca.send_keys(empresa)
                sleep(8)

                input_busca.send_keys(Keys.ENTER)
                sleep(4)

                span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
                cotacao_valor = span_val.text

                valores.append(cotacao_valor)
                data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

                print(f'Valor da cotação da {empresa}: {cotacao_valor}')
                codigos_empresas.append(empresa)
            else:
                print('Código inválido')

        dados = {
            'Data': data_hora,
            'Empresa': codigos_empresas,
            'Cotação': valores
            }

        self.__uol = pd.DataFrame(dados)
        self.__uol.set_index('Data', inplace=True)
        return self.__uol
