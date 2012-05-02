# -*- coding: utf-8 -*-
"""
Copyright (C) 2012 Fco. Javier Lucena Lucena (https://forja.rediris.es/users/franlu/)
Copyright (C) 2012 Serafín Vélez Barrera (https://forja.rediris.es/users/seravb/)
Copyright (C) 2012 Pablo Torres Anaya (https://forja.rediris.es/users/melon/)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation; either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU Affero General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""
import glob
import os
import sys

root_path = '/home/marina/cusl6-pupils/'

licencia_tochek = [
  'Copyright (C) 2012 Fco. Javier Lucena Lucena (https://forja.rediris.es/users/franlu/)\n',
  'Copyright (C) 2012 Serafín Vélez Barrera (https://forja.rediris.es/users/seravb/)\n',
  'This program is free software; you can redistribute it and/or\n',
  'modify it under the terms of the GNU Affero General Public License as\n',
  'published by the Free Software Foundation; either version 3 of the\n',
  'License, or (at your option) any later version.\n',
  'This program is distributed in the hope that it will be useful,\n',
  'but WITHOUT ANY WARRANTY; without even the implied warranty of\n',
  'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n',
  'General Public License for more details.\n',
  'You should have received a copy of the GNU Affero General Public\n',
  'License along with this program; if not, write to the\n',
  'Free Software Foundation, Inc., 59 Temple Place - Suite 330,\n',
  'Boston, MA 02111-1307, USA.\n']
licencia = [
  '# -*- coding: utf-8 -*-\n',
  '\"\"\"\n',
  'Copyright (C) 2012 Fco. Javier Lucena Lucena (https://forja.rediris.es/users/franlu/)\n',
  'Copyright (C) 2012 Serafín Vélez Barrera (https://forja.rediris.es/users/seravb/)\n',
  '\n',
  'This program is free software; you can redistribute it and/or\n',
  'modify it under the terms of the GNU Affero General Public License as\n',
  'published by the Free Software Foundation; either version 3 of the\n',
  'License, or (at your option) any later version.\n',
  '\n',
  'This program is distributed in the hope that it will be useful,\n',
  'but WITHOUT ANY WARRANTY; without even the implied warranty of\n',
  'MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU\n',
  'General Public License for more details.\n',
  '\n',
  'You should have received a copy of the GNU Affero General Public\n',
  'License along with this program; if not, write to the\n',
  'Free Software Foundation, Inc., 59 Temple Place - Suite 330,\n',
  'Boston, MA 02111-1307, USA.\n',
  '\"\"\"\n']
def poner_licencia(path):
  for dirname, dirnames, filenames in os.walk(path):
    for filename in filenames:
      ruta_fichero = os.path.join(dirname, filename)
      if '.py' in ruta_fichero and '.svn' not in ruta_fichero:
        f = open(ruta_fichero,'r+')
        old_file_lines = f.readlines()
        tiene_licencia = False
        for linea in old_file_lines:
          if linea in licencia_tochek:
            tiene_licencia = True
            break
        if not tiene_licencia:
          f.seek(0)
          for licencia_linea in licencia:
            f.write(licencia_linea)
          for old_linea in old_file_lines:
            if '# -*- coding: utf-8 -*-\n' not in old_linea:
              f.write(old_linea)
        f.close()
  return True
if (len(sys.argv) > 1):
  relative_dir = sys.argv[1]
  if relative_dir[len(relative_dir)-1] != '/':
    print "invalid argument"
    print "the last character of the path must be a '/'"
    print "example: python script_licencias.py ./"
  else:
    poner_licencia(relative_dir)
else:
  print "ERROR : invalid argument number"
  print "usage: python script_licencias.py <path>"
  print "example: python script_licencias.py ./"

