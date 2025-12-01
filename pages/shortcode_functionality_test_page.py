from playwright.sync_api import Page, expect
from conftest import base_url, table_url, table_name, table_description
from utils.table_data_utils import flextable_all_values

class ShortcodeFunctionalityTestPage:

    def __init__(self, page: Page):
        self.page = page
        self.page_url = '/shortcode-functionality-test-page'

        # Locators for creating the page
        self.add_page_url = '/wp-admin/post-new.php?post_type=page'
        self.new_page_title = 'shortcode functionality test page'
        self.new_page_add_title = page.get_by_role("textbox", name="Add title")
        self.new_page_publish_button = page.get_by_role("button", name="Publish", exact=True)
        self.new_page_editor_publish_button = page.get_by_label("Editor publish").get_by_role("button", name="Publish", exact=True)


        # Locators if Page not exists
        self.page_not_exists_title = 'Page not found'
        self.page_not_exists_message = page.get_by_text("Opps! The page you are looking for is missing")

        # Locator if Page exists
        self.edit_page_menuitem= page.get_by_role("menuitem", name=" Edit Page")
        self.adding_new_page_block= page.get_by_role("button", name="Add block")
        self.browse_all_block_option= page.get_by_role("button", name="Browse all. This will open")
        self.shortcode_option= page.get_by_role("option", name="Shortcode")
        self.shortcode_option_textbox= page.get_by_role("textbox", name="Shortcode text")
        self.page_save_button = page.get_by_role("button", name="Save", exact=True)
        self.page_shortcode_block_textfield_xpath = page.locator('//*[@id="blocks-shortcode-input-0"]')

        # Locator if Table exist
        self.table_title= page.get_by_role("heading", name=table_name)
        self.table_description= page.get_by_text(table_description)
        self.table_warper= self.page.locator("#create_tables_wrapper")
        self.entry_level_css_locator= page.locator('#create_tables_info')
        self.table_pagination_css_locator= page.locator('#create_tables_info')

        # Locator if Table Deleted
        self.table_deleted_text = page.get_by_role("heading", name="Table maybe deleted or can't")

        # Locator to test Layout
        self.main_content_container = page.locator("#content")
        self.problematic_table = page.locator(".gswpts_tables_content")
        self.problematic_column_xpath = page.locator('//article//table/tbody/tr[4]/td[*]')

        # Locators to test table matches the Google Sheet data
        self.table_data_1 = page.get_by_role("gridcell", name="Tahsin")
        self.table_data_2 = page.get_by_role("gridcell", name="Arafat")
        self.table_data_3 = page.get_by_role("gridcell", name="This exceptional product")
        self.table_data_4 = page.get_by_role("gridcell", name="https://example.com/72")

        # User Variables
        # Correct Variable Assignment (assuming you want to check all four locators)
        self.cell_value_01 = flextable_all_values[0]  # Tahsin
        self.cell_value_02 = flextable_all_values[7]  # Arafat
        self.cell_value_03 = flextable_all_values[6]  # This exceptional product...
        self.cell_value_04 = flextable_all_values[31]  # https://example.com/72 ⬅️ New variable




    def goto(self):
        self.page.goto(base_url+self.page_url)

    def page_not_exists(self):
        self.goto()
        page_not_exists = self.page_not_exists_message.is_visible(timeout=500)
        print("The Value Is::::::::", page_not_exists)
        return page_not_exists

    def create_page(self):
        self.page.goto(base_url+self.add_page_url)
        self.new_page_add_title.clear()
        self.new_page_add_title.fill(self.new_page_title)
        self.new_page_publish_button.click()
        self.new_page_editor_publish_button.click()

    def create_shortcode(self, shortcode:str):
        self.goto()
        self.edit_page_menuitem.click()
        self.adding_new_page_block.click()
        self.browse_all_block_option.click()
        self.shortcode_option.click()
        self.shortcode_option_textbox.click()
        self.shortcode_option_textbox.fill(shortcode)
        self.page_save_button.click()
        self.goto()
        # self.page.get_by_test_id("snackbar").get_by_role("link", name="View Page").click()

    def check_table_exist(self):
        expect(self.table_warper).to_be_visible()

    def check_shortcode_exist(self):
        if self.page_shortcode_block_textfield_xpath.is_visible():
            self.page_shortcode_block_textfield_xpath.clear()
        else:
            pass

    def table_match_with_google(self):
        expect(self.table_data_2).to_have_text(self.cell_value_02)
        expect(self.table_data_2).to_have_text(self.cell_value_02)
        expect(self.table_data_3).to_have_text(self.cell_value_03)
        expect(self.table_data_4).to_have_text(self.cell_value_04)

    def check_table_deleted(self):
        expect(self.table_warper).not_to_be_visible()
        expect(self.table_deleted_text).to_be_visible()

    def check_entry_level_exist(self):
        expect(self.entry_level_css_locator).to_be_visible()

    def check_pagination_exist(self):
        expect(self.table_pagination_css_locator).to_be_visible()

    def get_warper_width(self) -> float:
        box = self.table_warper.bounding_box()
        # Returns 0 if the element is not visible
        if box:
            return box['width']
        return 0.0

    def get_table_width(self) -> float:
        box = self.problematic_table.bounding_box()
        if box:
            return box['width']
        return 0.0

