# GitHub Action for text summarization

## Usage

Example usage of action in your workflow

### Example workflow

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action
      uses: Akshay090/text_summarization_action@master
      with:
        path: path/to/textFile.txt
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `path`  | Path to text file to be summarized    |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `summary`  | The summary of the text File which was processed    |

## Examples

### Using outputs

The outputs can be used whith other actions in workflow as given below, 

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Run action
      id: summary_action
      uses: Akshay090/text_summarization_action@master
      with:
        path: path/to/textFile.txt

    - name: Check outputs
      run: |
         echo "Text summary: ${{ steps.summary_action.outputs.summary }}"
```