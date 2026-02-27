// Target Interface (what your new system expects)
interface Printer {
    print(message: string): void;
}

// Adaptee (legacy class you cannot modify)
class OldPrinter {
    printOldFormat(text: string): void {
        console.log(`[OLD FORMAT] ${text.toUpperCase()}`);
    }
}

// TODO: Create PrinterAdapter class here
// Your adapter should implement Printer interface
// and use OldPrinter internally
class PrinterAdapter implements Printer {
    // TODO: Implement the adapter
    private oldPrinter : OldPrinter

    constructor( oldPrinter : OldPrinter) {
        this.oldPrinter=oldPrinter
    }
    print(message: string) : void {
        this.oldPrinter.printOldFormat(message)
    }

}