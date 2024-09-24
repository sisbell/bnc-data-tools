import os

from tools.ConversationWriter import ConversationWriter


def process_directory(data_dir, output_dir, writer):
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        if os.path.isdir(filepath):
            new_output_dir = os.path.join(output_dir, filename)
            process_directory(filepath, new_output_dir, writer)
        elif filename.endswith(".xml"):
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".txt")
            writer.convert(filepath, output_file)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "..", "data", "K")
    output_dir = os.path.join(script_dir, "..", "output")

    os.makedirs(output_dir, exist_ok=True)

    writer = ConversationWriter()
    process_directory(data_dir, output_dir, writer)
