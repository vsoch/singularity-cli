'''

Copyright (C) 2018 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2018 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from spython.logger import bot


    def build(self, image_path, spec_path, isolated=False, sandbox=False):
        '''build a singularity image, optionally for an isolated build
           (requires sudo)'''
        if self.debug is True:
            cmd = ['singularity','--debug','build']
        else:
            cmd = ['singularity','build']

        if isolated is True:
            cmd.append('--isolated')
        if sandbox is True:
            cmd.append('--sandbox')

        cmd = cmd + [image_path,spec_path]

        output = self.run_command(cmd,sudo=True)
        self.println(output)     
        return image_path

