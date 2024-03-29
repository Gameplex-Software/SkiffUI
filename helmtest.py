# ----------------------------------------------------------------------------
# SkiffUI Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

from shiphelm.helmdocker import helmdocker

hd = helmdocker() # create an instance of helmdocker
container_list = hd.get_running_containers() # call the method on the instance
print(container_list)
w=0

print("Preparing new server...")
while w<49:
    hd.run_container(image="docker/getting-started", detach=1)
    w=w+1

print("Your server is up and ready of connection!")