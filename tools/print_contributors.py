"""Update the table of contributors in the specification appendix.


Takes the content from the `.all-contributorsrc` file
to update the table of contributors names and contribution.

"""

from pathlib import Path

import emoji
from add_contributors import emoji_map, load_allcontrib, root_dir

output_file = Path(__file__).parent.parent / "src" / "appendices" / "contributors.md"


def contributor_table_header(max_name_length, max_contrib_length):
    return f"""\
| {"name":<{max_name_length}} | {"contributions":<{max_contrib_length}} |
| {"":-<{max_name_length}} | {"":-<{max_contrib_length}} |
"""


def create_line_contributor(
    contributor: dict[str, str], max_name_length: int, max_contrib_length: int
):
    name = contributor["name"]
    emap = emoji_map()
    contributions = "".join(
        emoji.emojize(emap[cont]) for cont in contributor["contributions"]
    )

    pad = max_contrib_length - len(contributor["contributions"]) * 2
    return f"| {name:<{max_name_length}} | {contributions}{'':<{pad}} |\n"


def main():
    allcontrib_file = root_dir().joinpath(".all-contributorsrc")
    allcontrib = load_allcontrib(allcontrib_file)

    allcontrib_names = [x["name"] for x in allcontrib["contributors"]]

    max_name_length = len(max(allcontrib_names, key=len))
    max_contrib_length = (
        max(len(x["contributions"]) for x in allcontrib["contributors"]) * 2
    )

    with open(output_file, "r", encoding="utf8") as f:
        content = f.readlines()

    with open(output_file, "w", encoding="utf8") as f:
        for line in content:
            if line.startswith("| name"):
                break
            f.write(line)

        f.write(contributor_table_header(max_name_length, max_contrib_length))

        for name in sorted(allcontrib_names):
            index_allcontrib = allcontrib_names.index(name)
            this_contrib = allcontrib["contributors"][index_allcontrib]
            f.write(
                create_line_contributor(
                    this_contrib, max_name_length, max_contrib_length
                )
            )


if __name__ == "__main__":
    main()
