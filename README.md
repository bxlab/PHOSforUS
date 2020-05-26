# PHOSforUS predictor usage guide

## 1. PHOSforUS features

PHOSforUS is a fully biophysical parameter-based protein phosphorylation site predictor.
From input sequences, it calculates 18 biophysical features, including:

- Horizontal features (6): Hydrophobicity, Secondary structure propensity, PII propensity, etc.
- Vertical features (4): AA molecular weight, residue charge, surface area, etc.
- eSCAPE thermodynamic features (8): dG, dHap, dHpol, TdS, etc.
   
All individual biophysical features are sent to sub-predictors, based on Naive Bayes classifier.
Resulting scores are sent to downstream metapredictor, based on gradient boosting classifier.
Prediction results are compiled into single result file per each sequence, which could be found in result_output folder.

## 2. System requirement

PHOSforUS is built on python 2.7 environment.
Along with base packages, it requires installation of numpy and scikit-learn package.

- numpy: 1.16.5
- scikit-learn: 0.20.3

After you fetched github repository, you can install PHOSforUS with setup.py:

    python setup.py install

Alternatively, you could use Conda to download PHOSforUS and its dependencies. It could be installed with conda run:

    conda install -c mcho22 phosforus 

Another option you could use is pip. It could be installed with pip as follow:

    pip install PHOSforUS

After you install the package, you could test the installation with this test script:

    from phosforus import phosforus
    phosforus.phosforus("ACDEFGHIKLMNPQRSTVWY", file_input = False, manual_input = True, verbose = True)

## 3. Usage samples

## (don't forget to import: from phosforus import phosforus)

### Option #1: phosforus.phosforus([filename])

If no other arguments other than input file name is given, PHOSforUS automatically targets for that file and predicts phosphorylation site. After prediction is completed, result file is generated in 'result_output/' folder. 
Sequence files should follow fasta format for smooth analysis. If multiple sequences are placed in a single file, PHOSforUS will predict phosphorylation sites in each of sequences but separate result files will be produced for each.

### Option #2: phosforus.phosforus([dirname], file_input = False, directory_input = True)

If directory input option is turned on, PHOSforUS will take all files in the given directory as sequence inputs. Beware not to include non-sequence files in the directory.

### Option #3: phosforus.phosforus(["manual sequence input"], file_input = False, manual_input = True)

If manual input option is turned on, PHOSforUS will take given sequence argument as a sequence input and proceed on prediction. It will not distinguish upper case and lower case letters. Letters other than 20 canonical amino acid codes would be recognized as random (X) amino acid.

## 4. Optional arguments

- verbose (default = False): if True, it will print prediction results on command line.

## 5. Result file format

PHOSforUS program would produce result file per each input protein sequence.
Result file includes following information.

Input sequence label (as in fasta file or manual input tag)

- Raw protein sequence
- Mapped phosphorylation sites in given sequence
- Site-wise details
   - Target site in the sequence
   - Target site type (S-, T-, Y, SP, TP)
   - Phosphorylation status (PHOSPHO / NONPHOS)
   - PHOSforUS prediction score
   - Converted phosphorylation probability

## 6. Alternative usage example: command line script (phosforus_cmd.py)

### Option #1: python phosforus_cmd.py [filename]

If no other arguments other than input file name is given, PHOSforUS automatically targets for that file and predicts phosphorylation site.

### Option #2: python phosforus_cmd.py [dirname] -d

If -d flag is given, PHOSforUS will take all files in the given directory as sequence inputs. 

### Option #3: python phosforus_cmd.py ["manual sequence input"] -m

If -m flag is given, PHOSforUS will take given sequence argument as a sequence input and proceed on prediction. 

### Optional argument: -v (verbose option)

If -v flag is given, it will print prediction results on command line.

## 7. Reproducibility-associated data

All accessory datasets & figure generation-associated scripts are stored in a separate repository.
https://github.com/mcho22/PHOSforUS_figure_resource
