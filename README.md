# DNA-project
design patterns

DNA Analyzer project / Sara Schimmel

Requirements:
DNA Analyzer System
Goal:
The goal of the system is to load, analyze, manipulate and save DNA sequences.
Description:
DNA sequences are composed of four types of nucleotides;
The nucleotides are marked A (Adenine), G (Guanine), C (Cytosine) and T (Thymine).
A full DNA molecule usually consists of two strands, connected to each other in
base-pair connections: As with Ts, and Cs with Gs.
Three successive nucleotides generate a codon, which might be chemically "read" in
various ways.
The system will interact with the user through a CLI (Command Line Interface) that
uses the standard I/O. Using that interface, the user will be able to load DNA
sequences from files, to analyze them, to manipulate them (e.g., by extracting
sequence slices or by modifying the sequence), and to store modified sequences and
reports.
The commands are detailed in the following sections.

*** For the full requirements description see "DNA Analyzer Project - Requirements.pdf" ***

Design patterns:
•	Factory – the main factory creates an object of a command type factory according to the command’s type
each command type factory creates the object of the specific command
•	Strategy – the parse class is a strategy class and gets a parse function according to the command type
•	Singleton – the database of all the sequences is a singleton class
Commands:
•	Creation commands:
-	New
-	Load
-	Dup
•	Manipulation commands:
-	Slice
-	Concat
•	Management commands:
-	Del
-	Save
•	Analysis commands:
-	Find
-	FindAll
-	Len
-	Count
•	Batch commands:
-	batchList
-	batchShow
-	batchSave
-	batchLoad
