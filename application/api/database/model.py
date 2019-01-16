import boto3
from zappa.async import task
import decimal

@task
def dynamodb_user_upload(attributes):
    the_dictionary = {}
    for item in attributes:
        # print(item)
        the_dictionary[item['Name']] = item['Value']
    the_dictionary['portfolio']=[]
    the_dictionary['account_value']=0
    the_dictionary['invested_amount']=0
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    try:
        table = client.Table('wasp_account')
        resp  = table.get_item(
            Key={"sub": the_dictionary['sub']}
        )
        return resp['Item']
    except KeyError:
        table=client.Table('wasp_account')
        table.put_item(
            Item=the_dictionary
        )

@task
def update_list_item(username,payment_id):
    product_name =(payment_id[0]['item_list']['items'][0]['name'])
    price        =(payment_id[0]['amount']['total'])
    currency_type=(payment_id[0]['amount']['currency'])
    sale_id      =(payment_id[0]['related_resources'][0]['sale']['id'])
    payment_mode =payment_id[0]['related_resources'][0]['sale']['payment_mode']
    #print(payment_id['transactions'])
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table = client.Table('wasp_account')
    response=table.update_item(
        Key={
            "sub":username
        },
        UpdateExpression="SET portfolio= list_append(portfolio, :r)",
        ExpressionAttributeValues={
            ':r':[{"product_id":product_name,
                 "amount_purchase":price,
                "payment_mode":payment_mode,
                "currency":currency_type,
                   "sales_id":sale_id}],
        },
        )
@task
def write_trans_item(username,transaction,infos):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table = client.Table('Transactions')
    resp=table.put_item(
        Item={  "id"          : transaction[0]['related_resources'][0]['sale']['id'],
                "product_name": transaction[0]['item_list']['items'][0]['name'],
                "p_r_name"    : transaction[0]['item_list']['items'][0]['sku'],
                "total"       : transaction[0]['amount']['total'],
                "created_time": transaction[0]['related_resources'][0]['sale']['create_time'],
                "currency"    : transaction[0]['amount']['currency'],
                "user_id"     : username,
                "f_name"      : infos['payer_info']['first_name'],
                "l_name"      : infos['payer_info']['last_name'],
                "bill_email"  : infos['payer_info']['email'],
                "payer_id"    : infos['payer_info']['payer_id']
              }
    )
@task
def update_prod_item(payment_id):
    product_name = (payment_id[0]['item_list']['items'][0]['name'])
    price        = (payment_id[0]['amount']['total'])
    client       = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table        = client.Table('product')
    response     = table.update_item(
        Key={
            "product_id": product_name
        },
        UpdateExpression = "set product_current_amount = product_current_amount + :val",
        ExpressionAttributeValues={
            ':val':decimal.Decimal(price)
        }
    )
@task
def update_invest_amount(username,payment_id):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    price = (payment_id[0]['amount']['total'])
    table = client.Table('wasp_account')
    response = table.update_item(
        Key={
            "sub":username
        },
        UpdateExpression = "set invested_amount = invested_amount + :val",
        ExpressionAttributeValues={
            ':val': decimal.Decimal(price)
        }
    )

def get_portfolio_item(username):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table  = client.Table('wasp_account')
    try:
        resp = table.get_item(
            Key={"sub": username}
        )
        return resp['Item']
    except KeyError:
        return False
def get_transactions_receipt(t_id):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table = client.Table('Transactions')
    try:
        resp = table.get_item(
            Key={"id": t_id}
        )
        return resp['Item']
    except KeyError:
        return False
@task
def update_percentage(prod_id):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table  = client.Table('product')
    try:
        resp = table.get_item(
            Key={"product_id": prod_id}
        )
        percentage=((resp['Item']['product_current_amount']/resp['Item']['product_fund_required']) *100)
        percentage=round(percentage,1)
        ta = table.update_item(
            Key={"product_id": prod_id
                 },
            UpdateExpression="set p_percentage_funded = :val",
            ExpressionAttributeValues={
                ':val': decimal.Decimal(percentage)
            }
        )
    except KeyError:
        return False

def get_table_item(product_name):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table  = client.Table('product')
    try:
        resp = table.get_item(
            Key={"product_id": product_name}
        )
        return resp['Item']
    except KeyError:
        return False


def get_all_items():
    client   = boto3.resource('dynamodb', region_name="ap-southeast-1")
    table    = client.Table('product')
    response = table.scan()
    return response

def add_subscriber_list(email):
    client = boto3.resource('dynamodb', region_name="ap-southeast-1")
    try:
        table = client.Table('newsletter')
        resp = table.get_item(
            Key={"email":email}
        )
        return resp['Item']
    except KeyError:
        table = client.Table('newsletter')
        table.put_item(
            Item={"email":email,
                  "status":"new"}
        )





