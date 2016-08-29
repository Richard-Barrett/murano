#    Copyright (c) 2016 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc


class ContractMethod(object):
    @abc.abstractmethod
    def transform(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def validate(self):
        raise NotImplementedError()

    def finalize(self):
        return self.value

    def check_type(self):
        return self.validate()

    def __getattr__(self, item):
        return self.context[item]


class ObjRef(object):
    def __init__(self, object_id):
        self.object_id = object_id