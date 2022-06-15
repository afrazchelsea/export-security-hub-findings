## Export AWS Security Hub Findings

Script to export your AWS Security Hub findings to a `.csv` file.

### Steps to execute -

- Clone this repository.
- Export your AWS account credentials in your Terminal OR select the SSO account where your Security Hub findings are present.
- Navigate to the root of the cloned repository.
- Run the following command - `make title="<---THE TITLE OF THE FINDING GOES HERE--->"` .

This will generate a `.csv` file with all the findings which can be later formatted in Microsoft Excel / Google Sheets, if needed.
