# Script for querying a cloud classifier hosted on the Classr MLaaS.
#
# Copyright (C) Saul Johnson 2023
# Author: Saul Johnson <saul.a.johnson@gmail.com>
# Usage: python3 classr_example.py
#
# Used for a 2023 guest lencture at NHL Stenden Leeuwarden.
# See requirements.txt for dependencies.

from classr import Classr


# Classify input from the user using our cloud classifier!
cloud_classifier = Classr('acd78708-850b-4cea-aeaa-23cec50d13b6')
document = input('Enter your input: ')
print(cloud_classifier.classify(document))
