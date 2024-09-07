import allure
from pycparser.ply.yacc import token
from conftest import *
import pytest
from page_objects.order_feed_page import OrderFeedPage
from locators.base_page_locators import BasePageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from page_objects.order_feed_page import OrderFeedPage
from data import Urls


class TestOrderFeedPage:

    @allure.title("Клик на заказ, откроется модальное окно")
    @allure.description("Перейти в ленту заказов. Запомнить номер заказа в ленте. Кликнуть по карточке этого заказа. Проверить что номер заказа в ленте совпадает с номером заказа в модальном окне")
    def test_order_feed_page_open_order(self, driver):
        feed_page = OrderFeedPage(driver)
        top_order_in_feed, order_in_modal = feed_page.feed_page_open_order()
        assert top_order_in_feed == order_in_modal

    @allure.title("Заказы пользователя из раздела История заказов отображаются на странице Лента заказов")
    @allure.description("Создать заказ, запомнить его номер. Перейти в ленту заказов. Сохранить состояние нахождения заказа в ленте true или false. Перейти в профиль, перейти в историю заказов. Сохранить состояние нахождения заказа в ленте true или false. Проверить, что оба значения сохраненных состояний в значении true, новый заказ отображается в истории и в ленте")
    def test_order_feed_order_in_history_exists_in_feed(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete):
        feed_page = OrderFeedPage(driver)
        is_order_in_feed, is_order_in_history = feed_page.feed_order_in_history_exists_in_feed()
        assert is_order_in_feed and is_order_in_history

    @allure.title("При создании нового заказа счетчики Выполнено за всё время и Выполнено за сегодня увеличиваются")
    @allure.description("Перейти в ленту заказов, сохранить значение счетчика. Перейти на главную страницу и создать новый заказ. Перейтив ленту заказов. Дождаться появления номера заказов в таблице В работе.Сохранить текущее значение счетчика. Проверить, что счетчик увеличился.")
    @pytest.mark.parametrize('counter', [OrderFeedPageLocators.counter_all_time, OrderFeedPageLocators.counter_today])
    def test_order_feed_page_counters_growth(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete, counter):
        feed_page = OrderFeedPage(driver)
        counter_after, counter_before = feed_page.feed_page_counters_growth(counter)
        assert counter_after > counter_before

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    @allure.description("Создать новый заказ. Перейти в ленту заказов. Сформировать значение элемента с номером заказа в таблице заказов В работе. Проверить отображение элемента в таблице В работе")
    def test_order_feed_page_order_number_in_status_box(self, driver, random_user_data, random_user_register, random_user_login, random_user_delete):
        feed_page = OrderFeedPage(driver)
        order_number = feed_page.feed_page_order_number_in_status_box()
        assert feed_page.is_displayed_order_in_status_box_in_process(order_number)