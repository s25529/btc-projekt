from django.shortcuts import render
from bitcoinlib.services.services import Service
from django.http import HttpResponse
from django.views.generic import TemplateView


def donation_list(request):

    service = Service(network="testnet")
    wallet_addr="tb1qnpsu96snc0206urdlevfv7tja6xtm573ygznyh"
    #tb1q9ye7nhnp4hdtudzjaanwq7lldxh5yy82kp6ytm"#"tb1q72qf8jjz796pmwngrw5ecy2ktq035jkat5jgd9"
    transactions = service.gettransactions(wallet_addr, "", 30)

    donators = []

    for transaction in transactions:
        donators.append(transaction.as_dict())


    sponsors = []

    for donator in donators:
        sponsors.append(donator['txid'])




    context = {"donators":sponsors, "address":wallet_addr}
    return render(request, 'donations/donate.html', context)