# Source: based on https://bskinn.github.io/Scan-PDF-Merging/

import itertools as itt
import sys

import PyPDF2 as PDF


def main():
    # get file paths from Automator
    doc1 = sys.argv[1]
    doc2 = sys.argv[2]
    
    # set output filename
    out = doc1.replace('.pdf', '') + '_merged.pdf'

    
    pdf_out = PDF.PdfFileWriter()

    with open(doc1, 'rb') as f_odd:
        with open(doc2, 'rb') as f_even:
            # Read files
            pdf_odd = PDF.PdfFileReader(f_odd)
            pdf_even = PDF.PdfFileReader(f_even)
            
            # Merge PDFs reversing the order of even pages
            for p in itt.chain.from_iterable(
                itt.zip_longest(
                    pdf_odd.pages,
                    reversed(pdf_even.pages),
                )
            ):
                if p:
                    pdf_out.addPage(p)
            
            # Write PDF to output file
            with open(out, 'wb') as f_out:
                pdf_out.write(f_out)

    return 0


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Wrong number of arguments!")
        sys.exit(1)

    sys.exit(main())
