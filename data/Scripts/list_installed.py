import subprocess
from dataclasses import dataclass

@dataclass
class Package:
    name: str
    version: str
    description: str
    architecture: str
    url: str
    licenses: list[str]
    groups: list[str]
    provides: list[str]
    depends_on: list[str]
    optional_deps: list[str]
    required_by: list[str]
    optional_for: list[str]
    conflicts_with: list[str]
    replaces: list[str]
    installed_size: str
    packager: str
    build_date: str
    install_date: str
    install_reason: str
    install_script: str
    validated_by: str

    def _clean(self, line: str, is_list: bool = False) -> str:
        x = line.split(": ")
        data = " ".join(x[1:])
        if is_list:
            if data == "None":
                return []
            else:
                return data.split("  ")
        else:
            if data == "None":
                return None
            else:
                return data.strip(" ")

    def __init__(self, data: list[str]):
        self.name = self._clean(data[0]) 
        self.version = self._clean(data[1]) 
        self.description = self._clean(data[2]) 
        self.architecture = self._clean(data[3])
        self.url = self._clean(data[4]) 
        self.licenses = self._clean(data[5], True)
        self.groups = self._clean(data[6], True)
        self.provides = self._clean(data[7], True)
        self.depends_on = self._clean(data[8], True)
        self.optional_deps = self._clean(data[9], True)
        self.required_by = self._clean(data[10], True)
        self.optional_for = self._clean(data[11], True)
        self.conflicts_with = self._clean(data[12], True)
        self.replaces = self._clean(data[13], True)
        self.installed_size = self._clean(data[14]) 
        self.packager = self._clean(data[15]) 
        self.build_date = self._clean(data[16]) 
        self.install_date = self._clean(data[17]) 
        self.install_reason = self._clean(data[18]) 
        self.install_script = self._clean(data[19])
        self.validated_by = self._clean(data[20]) 

def get_packages() -> list[Package]:
    p = subprocess.run(['pacman', '-Qi'], stdout=subprocess.PIPE)
    data = p.stdout.decode("utf-8")
    packages = []
    for i in data.split("\n\n"):
        lines = []
        for l in i.split("\n"):
            if l.find("  : ") != -1:
                lines.append(l)
            elif l == "":
                return packages
            else:
                lines[-1] += l
        packages.append(Package(lines))
    return packages

for i in get_packages():
    if i.install_reason == "Explicitly installed":
        print(i.name)
