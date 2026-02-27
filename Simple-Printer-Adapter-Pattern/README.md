# Simple Printer Adapter Pattern

## Problem Statement
<p>You have a legacy <code>OldPrinter</code> class that prints messages using a <code>printOldFormat(text: string)</code> method. Your new system expects all printers to implement the <code>Printer</code> interface with a <code>print(message: string)</code> method.</p>

<p>Your task is to create a <code>PrinterAdapter</code> class that makes the <code>OldPrinter</code> compatible with the new <code>Printer</code> interface without modifying the existing <code>OldPrinter</code> class.</p>

<h2><strong>Requirements</strong></h2>

<ol>
	<li>Create a <code>PrinterAdapter</code> class that implements the <code>Printer</code> interface</li>
	<li>The adapter should accept an <code>OldPrinter</code> instance in its constructor</li>
	<li>When <code>print(message: string)</code> is called on the adapter, it should internally call <code>printOldFormat(text: string)</code> on the <code>OldPrinter</code> instance</li>
	<li>Do not modify the <code>OldPrinter</code> class or <code>Printer</code> interface</li>
	<li>The adapter should properly forward the message to the legacy printer</li>
</ol>

## Input Format
A single line containing the message string to be printed

Hello World


## Output Format
A single line with the formatted output: [OLD FORMAT] <MESSAGE_IN_UPPERCASE>

[OLD FORMAT] HELLO WORLD


## Example
Example 1:
<b>Input</b>
<pre>Hello World</pre>
<b>Output</b>
<pre>[OLD FORMAT] HELLO WORLD</pre>
<b>Explanation</b>
<pre>The adapter receives "Hello World" through the print() method.
It forwards this to OldPrinter's printOldFormat() method.
The OldPrinter converts it to uppercase and adds the [OLD FORMAT] prefix.</pre>

Example 2:
<b>Input</b>
<pre>Design Patterns</pre>
<b>Output</b>
<pre>[OLD FORMAT] DESIGN PATTERNS</pre>
<b>Explanation</b>
<pre>The message "Design Patterns" is passed through the adapter.
The legacy printer formats it with uppercase conversion and prefix.</pre>

## Constraints
1 ≤ message length ≤ 1000
Message contains only printable ASCII characters
The OldPrinter class cannot be modified
You must use the Adapter design pattern

<b>Note:</b> The Adapter pattern is a structural design pattern that allows objects with incompatible interfaces to collaborate. In this problem, you're creating a wrapper that makes the legacy OldPrinter work with the modern Printer interface.

