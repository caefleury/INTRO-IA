# INTRO-IA
Código desenvolvido na matéria de introdução a inteligência artificial

## Project Structure

```
INTRO-IA/
├── src/              # Source code
│   ├── __init__.py
│   └── main.py       # Example main module
├── data/             # Data files (ignored by git except .gitkeep)
│   └── .gitkeep
├── .github/
│   └── workflows/
│       └── black.yml # GitHub Actions for Black formatting check
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
└── .gitignore        # Git ignore rules
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/caefleury/INTRO-IA.git
cd INTRO-IA
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

Run the example script:
```bash
python src/main.py
```

## Development

### Code Formatting

This project uses [Black](https://github.com/psf/black) for code formatting. To format your code:

```bash
black src/
```

To check formatting without making changes:
```bash
black --check src/
```

### Linting

This project uses [Flake8](https://flake8.pycqa.org/) for linting. To check your code:

```bash
flake8 src/
```

## CI/CD

GitHub Actions automatically checks Black formatting on every push and pull request to the main/master branch.
