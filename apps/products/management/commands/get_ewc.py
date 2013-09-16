# -*- coding: utf-8 -*-
# Copyright (C) 2013 OpenWeigh.co.uk
# Developer: Dairon Medina Caro <dairon.medina@gmail.com>
# Co-Developer Rhys Park <sales@openweigh.co.uk>
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Obtains list of European Waste Codes.'

    def handle(self, **options):
        pass
