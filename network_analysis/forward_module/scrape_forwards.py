import pandas as pd
import numpy as np
from telethon.sync import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputMessagesFilterPhotoVideo, Channel
from telethon.tl.functions.channels import GetFullChannelRequest
import json
import re
from telethon.errors import ChannelPrivateError
import pickle

credentials = {}

def define_cred(api_id, api_hash, phone, username):
    credentials['api_id'] = api_id
    credentials['api_hash']=api_hash
    credentials['phone']=phone
    credentials['username']=username

async def get_data_channel(channel_id, offset_date, names_dict, desc_dict, limit=None):
    """
    Get all messages from channel NEWER than offset date (e.g. sent after offset date)

    args:

    channel_id: id of channel to be scraped (has to be an integer), or channel username
    offset_date: date limit 
    names_dict: dict of id-to-names
    desc_dict: dict of id-to-bio
    
    return list of patcthed messages
    """

    if type(channel_id)==int:
    
        async with TelegramClient(credentials['username'], credentials['api_id'], credentials['api_hash']) as client:
                    entity = await client.get_entity(PeerChannel(channel_id))
                    full_entity = await client(GetFullChannelRequest(channel=entity))

                    names_dict[channel_id] = entity.title #get group name
                    desc_dict[channel_id] = full_entity.full_chat.about #get group bio

                    lista_mex = await client.get_messages(entity, reverse=True, offset_date=offset_date, limit=limit)
        
        return lista_mex

    elif type(channel_id)==str:
        async with TelegramClient(credentials['username'], credentials['api_id'], credentials['api_hash']) as client:
                    entity = await client.get_entity(f'https://t.me/{channel_id}')
                    full_entity = await client(GetFullChannelRequest(channel=entity))

                    names_dict[channel_id] = entity.title #get group name
                    desc_dict[channel_id] = full_entity.full_chat.about #get group bio

                    lista_mex = await client.get_messages(entity, reverse=True, offset_date=offset_date, limit=limit)
        
        return lista_mex


def get_channels_forward(lista_messaggi, receving_id):
    """
    lista_messaggi: list of patched telethon messages
    receving_id: id of the scraped group. So the forwarded_to id

    returns list of tuple with format (forwarded_from, forwarded_to)
    where forwarded_to is the receving_id

    """
    lista_fwd = []
    for mex in lista_messaggi:
        dict_mex = mex.to_dict()
        if 'fwd_from' in dict_mex.keys() and dict_mex['fwd_from'] is not None:
            fwd_info = dict_mex['fwd_from']['from_id']
            if type(fwd_info) == dict and fwd_info['_']=='PeerChannel':
                lista_fwd.append((fwd_info['channel_id'], receving_id))

    return lista_fwd
        