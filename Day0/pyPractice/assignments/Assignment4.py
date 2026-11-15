import builtins
import pydoc


def describe_builtin(name):
    """Return documentation text for a Python built-in name."""
    if not isinstance(name, str):
        return "Invalid value: name must be a string"

    if not hasattr(builtins, name):
        return f"No built-in named '{name}' found"

    builtin = getattr(builtins, name)
    return pydoc.render_doc(builtin, renderer=pydoc.plaintext)


if __name__ == "__main__":
    print(describe_builtin("len"))
