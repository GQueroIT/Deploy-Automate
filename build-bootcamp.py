#!/usr/bin/env python3
"""
Builds the IaC-Fundamentals-Bootcamp repo.
One repo, three sections: PowerShell, Bicep/ARM/JSON, Terraform.
Run this from wherever you want the repo folder to land, e.g.:
    python3 build_bootcamp.py
Safe to re-run - it won't overwrite files that already exist.
"""

from pathlib import Path

REPO_NAME = "IaC-Fundamentals-Bootcamp"

GLOSSARY_CONTENT = """# General IaC Concepts

**Infrastructure as Code (IaC)** - writing your servers, networks, and cloud resources as text files instead of clicking through a portal, so the setup can be saved, reused, and tracked like any other code.

**Declarative** - you describe what the end result should look like, and the tool figures out how to get there. This is how Bicep, ARM, and Terraform work.

**Imperative** - you write out every step in order to make something happen. This is how a PowerShell script works.

**State** - a record of what infrastructure already exists right now, so the tool knows what to change instead of rebuilding everything from scratch every time.

**Idempotent** - running the same thing twice gives you the same result the second time as the first. No duplicate resources, no surprise side effects.

**Provider** - the plugin that lets a tool talk to a specific platform. Terraform's azurerm provider is how Terraform talks to Azure.

**Resource** - a single thing being created or managed: a VM, a storage account, a virtual network.

**Module** - a reusable, packaged chunk of code you call instead of rewriting the same block over and over.

**Deployment** - the actual act of running your code against the cloud and creating or changing real resources.

# PowerShell

**Cmdlet** - pronounced "command-let." A built-in PowerShell command, always named Verb-Noun, like Get-Process or New-Item.

**Pipeline** - the | symbol. Takes the output of one cmdlet and feeds it straight into the next one as input.

**Object** - everything that comes out of a cmdlet in PowerShell is a structured object with properties, not plain text. That's what makes Get-Member and Where-Object work.

**Parameter** - a named input you pass into a cmdlet or function, like -Name or -Path.

**Variable** - a named container holding a value, always starts with $, like $name.

**Script** - a saved .ps1 file containing a sequence of PowerShell commands.

**Function** - a named, reusable block of code inside a script that you call with parameters.

# JSON and ARM

**JSON (JavaScript Object Notation)** - a plain text format for storing structured data as key-value pairs. ARM templates are written in this format.

**ARM template** - a JSON file describing the Azure resources you want deployed. Azure Resource Manager reads it and builds them.

**Resource provider** - the Azure service responsible for a resource type, written like Microsoft.Compute or Microsoft.Storage.

**API version** - a dated version string, like 2023-09-01, that tells Azure which version of a resource's schema you're using.

**Schema** - the shape a JSON file is supposed to follow: which fields are required, what type each value should be.

# Bicep

**Bicep** - a simpler language that compiles down into ARM JSON. You write Bicep, Azure still deploys ARM JSON underneath it.

**Decorator** - a tag starting with @ placed above a parameter to add a rule, like @allowed([...]) or @secure().

**Scope** - where a deployment targets: resource group, subscription, or management group.

**Interpolation** - dropping a variable's value directly inside a string using ${} syntax.

**Compile** - turning a .bicep file into the ARM JSON that actually gets deployed (az bicep build).

**Decompile** - the reverse: turning an existing ARM JSON template back into Bicep (az bicep decompile).

# Terraform

**HCL (HashiCorp Configuration Language)** - the language Terraform files are written in, ending in .tf.

**Resource block** - the chunk of HCL defining one piece of infrastructure to create.

**State file** - a JSON file Terraform keeps (terraform.tfstate) tracking what it has already built, so it knows what's real versus what's just in your code.

**Plan** - a preview of what Terraform would change, generated with terraform plan, before anything actually happens.

**Apply** - the command that takes the plan and actually creates or changes the real resources.

**Data source** - a way to pull in information about something that already exists, without Terraform managing or creating it.

**count / for_each** - meta-arguments that let one resource block create multiple copies of itself from a number or a list.
"""

# (section_folder, section_title, [(slug, title, solution_ext), ...])
SECTIONS = [
    (
        "powershell",
        "PowerShell",
        [
            ("01-variables-and-output", "Variables, Data Types, and Output", "ps1"),
            ("02-control-flow", "Control Flow: If/Else, Switch, Loops", "ps1"),
            ("03-functions", "Functions: Params, Return Values, Scope", "ps1"),
            ("04-arrays-and-hashtables", "Arrays and Hashtables", "ps1"),
            ("05-the-pipeline", "The Pipeline: Where-Object, Sort-Object, Select-Object", "ps1"),
            ("06-string-manipulation", "String Manipulation and Formatting", "ps1"),
            ("07-error-handling", "Error Handling: Try/Catch/Finally", "ps1"),
            ("08-files-and-csv", "Files: Get-Content, Set-Content, CSV Import/Export", "ps1"),
            ("09-json-in-powershell", "JSON in PowerShell: ConvertTo-Json / ConvertFrom-Json", "ps1"),
            ("10-script-structure", "Script Structure: Params Blocks, Comment-Based Help", "ps1"),
            ("11-az-powershell-basics", "Az PowerShell Module Basics", "ps1"),
        ],
    ),
    (
        "bicep-arm-json",
        "Bicep, ARM, and JSON",
        [
            ("01-arm-json-anatomy", "ARM JSON Anatomy", "json"),
            ("02-bicep-basics", "Bicep Basics: JSON to Bicep", "bicep"),
            ("03-parameters-and-variables", "Parameters and Variables", "bicep"),
            ("04-outputs", "Outputs", "bicep"),
            ("05-expressions-and-functions", "Expressions and Built-In Functions", "bicep"),
            ("06-conditionals-and-loops", "Conditionals and Loops", "bicep"),
            ("07-modules", "Modules", "bicep"),
            ("08-dependencies", "Dependencies: Implicit vs Explicit", "bicep"),
            ("09-array-loops-multiple-resources", "Array Loops for Multiple Resources", "bicep"),
            ("10-deployment-scopes", "Deployment Scopes", "bicep"),
            ("11-what-if-and-validation", "What-If and Validation Workflow", "bicep"),
            ("12-decompile-arm-to-bicep", "Decompiling ARM to Bicep", "bicep"),
        ],
    ),
    (
        "terraform",
        "Terraform",
        [
            ("01-iac-concepts-and-providers", "IaC Concepts, Providers, Resource Blocks", "tf"),
            ("02-core-workflow", "Core Workflow: Init, Plan, Apply, Destroy", "tf"),
            ("03-variables-and-outputs", "Variables and Outputs", "tf"),
            ("04-state", "State: What It Is and Why It Matters", "tf"),
            ("05-azurerm-provider", "The azurerm Provider", "tf"),
            ("06-resource-dependencies", "Resource Dependencies", "tf"),
            ("07-data-sources", "Data Sources", "tf"),
            ("08-count-and-for-each", "count and for_each", "tf"),
            ("09-modules", "Writing and Calling Modules", "tf"),
            ("10-remote-state-basics", "Remote State Basics (HCP Terraform)", "tf"),
            ("11-lifecycle-blocks", "Lifecycle Blocks", "tf"),
            ("12-plan-output-and-state-commands", "Reading Plan Output and terraform state Commands", "tf"),
        ],
    ),
]


def lesson_content(title: str) -> str:
    return f"""# {title}

## Status
Not started

## Lesson
(To be filled in when you start this module.)

## Key Terms
See GLOSSARY.md at the repo root for terms used in this module.
"""


def problem_content(title: str) -> str:
    return f"""# Problem: {title}

(Problem to be added when you start this module.)
"""


def solution_content(ext: str) -> str:
    comment = "#" if ext in ("ps1", "tf") else "//"
    return f"{comment} Solution - write your work here\n"


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content)
    return True


def build():
    base = Path(REPO_NAME)
    base.mkdir(exist_ok=True)

    write_if_missing(base / "GLOSSARY.md", GLOSSARY_CONTENT)

    readme_lines = [
        "# IaC Fundamentals Bootcamp",
        "",
        "Hands-on bootcamp covering PowerShell, Bicep/ARM/JSON, and Terraform in one repo.",
        "Each module has a lesson.md, a problem.md, and a solution file. Work modules in any order.",
        "See GLOSSARY.md for terminology.",
        "",
    ]

    created = 0
    for folder, title, modules in SECTIONS:
        section_path = base / folder
        section_path.mkdir(exist_ok=True)
        readme_lines.append(f"# {title}")
        readme_lines.append("")
        for slug, mod_title, ext in modules:
            module_path = section_path / slug
            module_path.mkdir(exist_ok=True)
            if write_if_missing(module_path / "lesson.md", lesson_content(mod_title)):
                created += 1
            if write_if_missing(module_path / "problem.md", problem_content(mod_title)):
                created += 1
            if write_if_missing(module_path / f"solution.{ext}", solution_content(ext)):
                created += 1
            readme_lines.append(f"- [ ] {slug}: {mod_title}")
        readme_lines.append("")

    write_if_missing(base / "README.md", "\n".join(readme_lines))

    total_modules = sum(len(m) for _, _, m in SECTIONS)
    print(f"Built {REPO_NAME}/")
    print(f"  {len(SECTIONS)} sections, {total_modules} modules, {created} files written.")


if __name__ == "__main__":
    build()