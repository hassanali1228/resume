import toml
from latex_reserve import *

class ResumeWriter:
    def __init__(self) -> None:
        self.latex_str = ""
        self.dent = 0
    
    def add_line(self, line: str) -> None:
        self.latex_str += "  " * self.dent + line + "\n"

    def indent(self, value: int=1) -> None:
        self.dent += value

    def dedent(self, value: int =1) -> None:
        self.dent -= value


def add_profile(writer: ResumeWriter, profile: dict[str, str | dict[str, str]]) -> None:
    writer.add_line("\\begin{resume_header}")
    writer.add_line(
        f"\\name{{\\textbf{{{profile['name']}}}}} \\vspace{{0.02in}}"
    )
    writer.add_line("\\contact{")
    writer.indent()

    for idx, link in enumerate(profile["links"]):
        if 'url' in link:
            line = f"\\fa{link['favicon']}\enspace \href{{{link['url']}}}{{{link['display']}}}"
        else:
            line = f"\\fa{link['favicon']}\enspace {link['display']}"

        if idx != len(profile["links"]) - 1: line += " \hspace{0.3in} \\"
        else: line += " \\"

        writer.add_line(line)

    writer.dedent()
    writer.add_line("}")
    writer.add_line("\\end{resume_header}")

def add_skills(writer: ResumeWriter, skills: dict[str, list[str]]) -> None:
    writer.add_line("\\begin{resume_section}{Skills}")
    writer.indent()
    writer.add_line("\\begin{nospacetabbing}")
    for idx, (category, skill_list) in enumerate(skills.items()):
        skill_str = f"\\textbf{{\\color{{darkblue}}{category}:}} \= "
        skill_str += ", ".join(skill_list)
        if idx != len(skills) - 1:
            skill_str += " \\\\[1pt]"
        else:
            skill_str += " \\\\*"
        writer.add_line(skill_str)

    writer.add_line("\\vspace{2pt}")
    writer.add_line("\\end{nospacetabbing}")
    writer.dedent()

    writer.add_line("\\end{resume_section}")


def parse_role_table(table: dict) -> dict:
    role_table = {}
    for role, val in table.items():
        if isinstance(val, str) and val in table.keys():
            role_table[role] = table[val]
        else:
            role_table[role] = val
    return role_table

def add_work_experience(writer: ResumeWriter, include_mission: bool, experience: dict[str, str | list[str] | dict[str, list[int]]], role: str) -> None:
    writer.add_line("\\begin{resume_employer}")
    writer.indent()
    writer.add_line(
        f"{{\\color{{darkblue}} {experience['company']} - \\normalfont {experience['mission']}}}"
        if include_mission
        else f"{{\\color{{darkblue}} {experience['company']}}}"
    )

    title_table = parse_role_table(experience["title"])
    writer.add_line(
        f"{{{title_table[role]}}}"
    )
    writer.add_line(
        f"{{{experience['location']}}} {{{experience['date_range']}}} \\vspace{{3 pt}}"
    )

    order_table = parse_role_table(experience["order"])
    for idx in order_table[role]:
        writer.add_line(f"\\item {experience['content'][idx]}")

    writer.dedent()
    writer.add_line("\\end{resume_employer}")

def add_project(writer: ResumeWriter, project: dict[str, list[str]]) -> None:
    line = "\\begin{resume_subsection} "
    tool_list = ", ".join(project["tools"])
    if "url" not in project:
        line += f"{{\\textcolor{{darkblue}} {{{project['name']}}} "
        line += f"\color{{black}} - {tool_list}}}"
    else:
        line += f"{{\href{{{project['url']}}}{{\\textcolor{{darkblue}}{{{project['name']}}}"
        line += f"\color{{black}} - {tool_list} \\faicon{{{project['favicon']}}}}}}}"
    writer.add_line(line)

    writer.indent()
    writer.add_line("\\begin{subitems}")
    for item in project["content"]:
        writer.add_line(f"\\item {item}")
    writer.dedent()
    writer.add_line("\\end{subitems}")
    writer.add_line("\\end{resume_subsection}")

def generator(enable_grayscale: bool, include_mission: bool, education_first: bool, role: str) -> str:
    resume_writer = ResumeWriter()

    resume_writer.latex_str += start

    if enable_grayscale:
        resume_writer.latex_str += grayscale

    resume_writer.latex_str += template_definitions
    resume_writer.add_line("")

    add_profile(resume_writer, toml_dict["profile"])
    resume_writer.add_line("")

    if education_first:
        resume_writer.latex_str += education
    else:
        add_skills(resume_writer, toml_dict["skills"])
        resume_writer.add_line("")

    resume_writer.add_line("\\begin{resume_section}{Work Experience}")
    resume_writer.add_line("")
    resume_writer.indent()

    for work_experience in toml_dict["work_experiences"]:
        add_work_experience(
            resume_writer,
            include_mission,
            work_experience,
            role
        )
        resume_writer.add_line("")

    resume_writer.dedent()
    resume_writer.add_line("\\end{resume_section}")

    resume_writer.add_line("\\begin{resume_section}{Personal Projects}")
    resume_writer.add_line("")
    resume_writer.indent()

    for project in toml_dict["projects"]:
        add_project(resume_writer, project)
        resume_writer.add_line("")

    resume_writer.dedent()
    resume_writer.add_line("\\end{resume_section}")

    if education_first:
        add_skills(resume_writer, toml_dict["skills"])
        resume_writer.add_line("")
    else:
        resume_writer.latex_str += education

    resume_writer.latex_str += end

    return resume_writer.latex_str

if __name__ == "__main__":
    toml_dict = toml.load("resume.toml")

    print(
        generator(**toml_dict["config"])
    )
