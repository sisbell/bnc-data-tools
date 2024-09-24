import os
import xml.etree.ElementTree as ET


class ConversationWriter:

    def convert(self, input_file, output_file_name):
        print(F"Processing {input_file}")
        tree = ET.parse(input_file)
        if tree.find('.//classCode').text != "S conv":
            return

        speaker_dict = self.read_speaker_dict(tree)
        setting_dict = self.read_setting_dict(tree)
        conversations_dict = self.read_conversations_dict(tree, speaker_dict)
        settings_ids = [div.attrib.get('n') for conversation in tree.findall('.//stext[@type="CONVRSN"]')
                        for div in conversation.findall('div')]

        output_dir = os.path.dirname(output_file_name)
        os.makedirs(output_dir, exist_ok=True)
        with open(output_file_name, 'w') as output_file:
            for setting_id in settings_ids:
                if setting_id in setting_dict:
                    output_file.write(f"---| {setting_dict[setting_id]}")
                else:
                    output_file.write("---")
                for sentence in conversations_dict[setting_id]:
                    output_file.write(f"\n{sentence}")
                output_file.write("\n\n")

    @staticmethod
    def read_setting_dict(element_tree: ET.ElementTree):
        setting_dict = {}
        for setting in element_tree.findall('.//setting'):
            setting_id = setting.attrib.get('n')
            try:
                setting_locale = setting.find("locale").text.strip()
            except AttributeError:
                setting_locale = "N/A"
            setting_activity = setting.find("activity").text.strip()
            setting_uuid = setting.get('{http://www.w3.org/XML/1998/namespace}id')
            setting_dict[setting_id] = f"{setting_uuid} | {setting_id} | {setting_locale} | {setting_activity}"
        return setting_dict

    @staticmethod
    def read_speaker_dict(element_tree: ET.ElementTree):
        speaker_dict = {}
        for person in element_tree.findall('.//person'):
            person_id = person.attrib.get('{http://www.w3.org/XML/1998/namespace}id')
            person_name = person.find("persName").text
            speaker_dict[person_id] = person_name
        return speaker_dict

    @staticmethod
    def read_conversations_dict(element_tree: ET.ElementTree, speaker_dict: dict):
        conversations_dict = {}
        for conversation in element_tree.findall('.//stext[@type="CONVRSN"]'):
            for div in conversation.findall('div'):
                div_n = div.attrib.get('n')
                sentences = []
                conversations_dict[div_n] = sentences
                for u in div.findall('u'):
                    speaker_id = u.attrib.get('who')
                    for sentence in u.findall('s'):
                        sentence_text = ''.join(element.text for element in sentence if element.text)
                        if speaker_id in speaker_dict:
                            speaker_name = speaker_dict[speaker_id]
                        else:
                            speaker_name = speaker_id
                        sentences.append(f"{speaker_name}: {sentence_text}")
        return conversations_dict
