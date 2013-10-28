Idea to find the vendor and application from CVEs

REQUIREMENTS:

    pip install xmltodict


Example:

    $ python ref.py | tail -10


```
CVE-2013-6129
[[u'vbulletin', u'vbulletin', u'4.1'], [u'vbulletin', u'vbulletin', u'5.0']]
CVE-2013-6170
[[u'juniper', u'junos', u'10.0'], [u'juniper', u'junos', u'11.1'], [u'juniper', u'junos', u'11.2'], [u'juniper', u'junos', u'10.4'], [u'juniper', u'junos', u'11.4']]
CVE-2013-6170
[[u'juniper', u'junos', u'10.0'], [u'juniper', u'junos', u'11.1'], [u'juniper', u'junos', u'11.2'], [u'juniper', u'junos', u'10.4'], [u'juniper', u'junos', u'11.4']]
CVE-2013-6243
[[u'landing_pages_project', u'landing_pages_plugin', u'1.0.8.5', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.9.3', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.9.0', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.7.1', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.7.9', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.5.1', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.1', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.5.6', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.5.3', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.3.7', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.3.9', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.3.8', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.2.3', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.2.1', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.1.7', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.1.8', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.1.9', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.7.3', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.4.2', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.9.4', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.4.4', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.8.6', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.4.1', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.8.1', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.9.9', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.0.8.4', u'-', u'~~~wordpress~~'], [u'landing_pages_project', u'landing_pages_plugin', u'1.1.0.1', u'-', u'~~~wordpress~~']]
CVE-2013-6244
[[u'sap', u'netweaver', u'7.03'], [u'sap', u'netweaver', u'7.01'], [u'sap', u'netweaver', u'6.4'], [u'sap', u'netweaver', u'4.0'], [u'sap', u'netweaver', u'7.30'], [u'sap', u'netweaver', u'7.02'], [u'sap', u'netweaver', u'7.0'], [u'sap', u'netweaver', u'7.31'], [u'sap', u'netweaver', u'7.10']]
```
