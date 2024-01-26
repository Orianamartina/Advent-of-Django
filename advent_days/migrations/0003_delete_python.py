# Generated by Django 5.0 on 2024-01-26 18:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models



class Migration(migrations.Migration):


    dependencies = [
        ("advent_days", "0002_initial")
    ]
    

    def create(apps, schema_editor):
        programming_languages = [
        "Python",
        "JavaScript",
        "Java",
        "C#",
        "C++",
        "PHP",
        "TypeScript",
        "C",
        "Swift",
        "Objective-C",
        "Ruby",
        "Kotlin",
        "Go",
        "R",
        "Shell",
        "MATLAB",
        "Scala",
        "Rust",
        "Groovy",
        "Perl",
        "HTML/CSS",
        "Dart",
        "Lua",
        "Haskell",
        "Julia",
        "TypeScript",
        "Shell",
        "PowerShell",
        "Visual Basic",
        "Apex (Salesforce)",
        "ABAP (SAP)",
        "COBOL",
        "Fortran",
        "Ada",
        "Lisp",
        "Scheme",
        "Erlang",
        "Tcl",
        "Prolog",
        "PL/SQL",
        "Apex (Salesforce)",
        "COBOL",
        "Fortran",
        "Ada",
        "Lisp",
        "Scheme",
        "Erlang",
        "Tcl",
        "Prolog",
        "PL/SQL"
        ]
        languages = apps.get_model('advent_days', 'Language')
        for l in programming_languages:
            languages.objects.create(name=l)


    operations = [migrations.RunPython(create)]
