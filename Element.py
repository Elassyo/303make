
class Element:
    def __init__(self, line):
        spl = line.split(":")
        self._name = spl[0].strip()
        self._deps = []
        self.cline = ""
        for dep in spl[1].split():
            dep = dep.strip()
            if not dep:
                continue
            self._deps.append(dep)

    def is_dep(self, dep):
        return 1 if dep in self._deps else 0

    def __repr__(self):
        return self._name + ": " + " ".join(self._deps)

    def __eq__(self, other):
        return other == self._name
