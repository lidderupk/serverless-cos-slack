from ibm_botocore.client import Config
import ibm_boto3
import subprocess

from xlrd import open_workbook


def main(dict):

    client = ibm_boto3.client('s3',
                              ibm_api_key_id=dict['apikey'],
                              ibm_service_instance_id=dict['resource_instance_id'],
                              ibm_auth_endpoint=dict['auth_endpoint'],
                              config=Config(signature_version='oauth'),
                              endpoint_url=dict['service_endpoint'])

    download_file_path = './sf.xls'
    try:
        try:
            client.download_file(
                dict['bucket_name'], dict['object_name'], download_file_path)
        except Exception as e:
            raise
        else:
            print('File Downloaded')

            # ls the directory to log out the files.
            # print(subprocess.call(["ls", "-l"]))

            return analyse_file(download_file_path)

    except Exception as e:
        print(e)
        return {"status": "error"}


def analyse_file(path):
    try:
        f = open_workbook(path)
    except FileNotFoundError as e:
        raise
    else:
        for sheet in f.sheets():
            # print rows in each sheet !
            print(sheet.nrows)

            # this is where you can analyze the file data and return
            # a dictionary to the next action
            return {"sheet.nrows": sheet.nrows}


if __name__ == "__main__":
    main({})
