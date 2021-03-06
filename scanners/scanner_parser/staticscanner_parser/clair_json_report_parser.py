#                   _
#    /\            | |
#   /  \   _ __ ___| |__   ___ _ __ _   _
#  / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
# / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                    __/ |
#                                   |___/
# Copyright (C) 2017-2018 ArcherySec
# This file is part of ArcherySec Project.


from staticscanners.models import clair_scan_db, clair_scan_results_db
import uuid
import hashlib
from datetime import datetime


def clair_report_json(data, project_id, scan_id):
    """

    :param data:
    :param project_id:
    :param scan_id:
    :return:
    """

    global vul_col
    try:
        high = data['Vulnerabilities']['High']
        for vuln in high:
            vul_id = uuid.uuid4()
            Name = vuln['Name']
            NamespaceName = vuln['NamespaceName']
            Description = vuln['Description']
            Link = vuln['Link']
            Severity = vuln['Severity']
            Metadata = vuln['Metadata']
            FeatureName = vuln['FeatureName']
            FeatureVersion = vuln['FeatureVersion']

            if Severity == "High":
                vul_col = "important"

            dup_data = Name + Severity + NamespaceName

            duplicate_hash = hashlib.sha256(dup_data).hexdigest()

            match_dup = clair_scan_results_db.objects.filter(
                dup_hash=duplicate_hash).values('dup_hash')
            lenth_match = len(match_dup)

            if lenth_match == 1:
                duplicate_vuln = 'Yes'
            elif lenth_match == 0:
                duplicate_vuln = 'No'
            else:
                duplicate_vuln = 'None'

            false_p = clair_scan_results_db.objects.filter(
                false_positive_hash=duplicate_hash)
            fp_lenth_match = len(false_p)

            if fp_lenth_match == 1:
                false_positive = 'Yes'
            else:
                false_positive = 'No'

            save_all = clair_scan_results_db(
                vuln_id=vul_id,
                scan_id=scan_id,
                project_id=project_id,
                Name=Name,
                NamespaceName=NamespaceName,
                Description=Description,
                Link=Link,
                Severity=Severity,
                Metadata=Metadata,
                FeatureName=FeatureName,
                FeatureVersion=FeatureVersion,
                vuln_status='Open',
                dup_hash=duplicate_hash,
                vuln_duplicate=duplicate_vuln,
                false_positive=false_positive,
                vul_col=vul_col,
            )
            save_all.save()
    except Exception:
        print "High Vulnerability Not Found"
        pass

    try:

        medium = data['Vulnerabilities']['Medium']
        for vuln in medium:
            vul_id = uuid.uuid4()
            Name = vuln['Name']
            NamespaceName = vuln['NamespaceName']
            Description = vuln['Description']
            Link = vuln['Link']
            Severity = vuln['Severity']
            Metadata = vuln['Metadata']
            FeatureName = vuln['FeatureName']
            FeatureVersion = vuln['FeatureVersion']

            if Severity == "Medium":
                vul_col = "warning"

            dup_data = Name + Severity + NamespaceName

            duplicate_hash = hashlib.sha256(dup_data).hexdigest()

            match_dup = clair_scan_results_db.objects.filter(
                dup_hash=duplicate_hash).values('dup_hash')
            lenth_match = len(match_dup)

            if lenth_match == 1:
                duplicate_vuln = 'Yes'
            elif lenth_match == 0:
                duplicate_vuln = 'No'
            else:
                duplicate_vuln = 'None'

            false_p = clair_scan_results_db.objects.filter(
                false_positive_hash=duplicate_hash)
            fp_lenth_match = len(false_p)

            if fp_lenth_match == 1:
                false_positive = 'Yes'
            else:
                false_positive = 'No'

            save_all = clair_scan_results_db(
                vuln_id=vul_id,
                scan_id=scan_id,
                project_id=project_id,
                Name=Name,
                NamespaceName=NamespaceName,
                Description=Description,
                Link=Link,
                Severity=Severity,
                Metadata=Metadata,
                FeatureName=FeatureName,
                FeatureVersion=FeatureVersion,
                vuln_status='Open',
                dup_hash=duplicate_hash,
                vuln_duplicate=duplicate_vuln,
                false_positive=false_positive,
                vul_col=vul_col,
            )
            save_all.save()
    except Exception:
        print "Medium Vulnerability not found."
        pass

    try:
        low = data['Vulnerabilities']['Low']

        for vuln in low:
            vul_id = uuid.uuid4()
            Name = vuln['Name']
            NamespaceName = vuln['NamespaceName']
            Description = vuln['Description']
            Link = vuln['Link']
            Severity = vuln['Severity']
            Metadata = vuln['Metadata']
            FeatureName = vuln['FeatureName']
            FeatureVersion = vuln['FeatureVersion']

            if Severity == "Low":
                vul_col = "info"

            dup_data = Name + Severity + NamespaceName

            duplicate_hash = hashlib.sha256(dup_data).hexdigest()

            match_dup = clair_scan_results_db.objects.filter(
                dup_hash=duplicate_hash).values('dup_hash')
            lenth_match = len(match_dup)

            if lenth_match == 1:
                duplicate_vuln = 'Yes'
            elif lenth_match == 0:
                duplicate_vuln = 'No'
            else:
                duplicate_vuln = 'None'

            false_p = clair_scan_results_db.objects.filter(
                false_positive_hash=duplicate_hash)
            fp_lenth_match = len(false_p)

            if fp_lenth_match == 1:
                false_positive = 'Yes'
            else:
                false_positive = 'No'

            save_all = clair_scan_results_db(
                vuln_id=vul_id,
                scan_id=scan_id,
                project_id=project_id,
                Name=Name,
                NamespaceName=NamespaceName,
                Description=Description,
                Link=Link,
                Severity=Severity,
                Metadata=Metadata,
                FeatureName=FeatureName,
                FeatureVersion=FeatureVersion,
                vuln_status='Open',
                dup_hash=duplicate_hash,
                vuln_duplicate=duplicate_vuln,
                false_positive=false_positive,
                vul_col=vul_col,
            )
            save_all.save()
    except Exception:
        print "Low Vulnerability Not found"
        pass

    all_clair_data = clair_scan_results_db.objects.filter(scan_id=scan_id)

    total_vul = len(all_clair_data)
    total_high = len(all_clair_data.filter(Severity='High'))
    total_medium = len(all_clair_data.filter(Severity='Medium'))
    total_low = len(all_clair_data.filter(Severity='Low'))
    total_duplicate = len(all_clair_data.filter(vuln_duplicate='Yes'))

    clair_scan_db.objects.filter(scan_id=scan_id).update(
        total_vuln=total_vul,
        SEVERITY_HIGH=total_high,
        SEVERITY_MEDIUM=total_medium,
        SEVERITY_LOW=total_low,
        total_dup=total_duplicate
    )
