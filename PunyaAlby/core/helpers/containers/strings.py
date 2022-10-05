class Strings(object):
    def close_tab_string(self):
        text = "Selamat datang di ALBY-PYROBOT.\n"
        text += "Ini adalah Menu Help Anda, Ketuk tombol buka untuk mendapatkan lebih banyak tombol,\n"
        text += "yang akan membantu anda untuk memahami pengoperasian userbot & asisten anda ( ALBY )\n"
        text += "\n\n• Menu Ditutup"

        return text



    def home_tab_string(self):
        text = "**Dex:** Home\n\n"
        text += "**Description:** Ini adalah menu help yang Anda gunakan untuk menavigasi setiap tombol yang berbeda ke informasi.."

        return text



    def plugin_tab_string(self):
        text = "**Dex:** Plugins \n\n"
        text += "**Location:** /home/plugins\n\n"
        text += f"**Plugins:** `{len(self.CMD_HELP)}`"

        return text


    def ialive_tab_string(self):
        text = f"**⛊  Inline Status:**\n\n"
        text += f"**⟐** {self.USER_BIO}\n\n"
        text += f"**⟜ Owner**: [{self.name}](https://t.me/{self.username})\n"
        text += f"**⟜ ALBY-PYROBOT:** `{self.userbot_version}`\n"
        text += f"**⟜ Python:** `{self.python_version}`\n"
        text += f"**⟜ Pyrogram:** `{self.pyrogram_version}`\n"
        text += f"**⟜ uptime:** `{self.uptime()}`\n"

        return text



    def pmpermit_tab_string(self):
        text = "Not implemented yet."

        return text
