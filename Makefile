run:
	rm -rf ./raw_findings.json ./FormattedFindings.csv
	aws securityhub get-findings --filters '{"WorkflowStatus":[{"Value":"NEW","Comparison":"EQUALS"}],"Title":[{"Value":"$(title)","Comparison":"EQUALS"}],"ComplianceStatus":[{"Value":"FAILED","Comparison":"EQUALS"}]}' >> raw_findings.json
	python script.py

.DEFAULT_GOAL := run