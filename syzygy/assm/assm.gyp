# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    'chromium_code': 1,
  },
  'targets': [
    {
      'target_name': 'asm_lib',
      'type': 'static_library',
      'sources': [
        'assembler_base.h',
        'assembler_base_impl.h',
        'assembler.h',
        'cond.h',
        'const.h',
        'label_base.h',
        'operand_base.h',
        'register_internal.h',
        'register.cc',
        'register.h',
        'value_base.h',
      ],
      'dependencies': [
        '<(src)/base/base.gyp:base',
        '<(src)/syzygy/common/common.gyp:common_lib',
      ],
    },
    {
      'target_name': 'asm_unittests',
      'type': 'executable',
      'sources': [
        'assembler_unittest.cc',
        'register_unittest.cc',
        '<(src)/base/test/run_all_unittests.cc',
      ],
      'dependencies': [
        'asm_lib',
        '<(src)/syzygy/core/core.gyp:core_lib',
        '<(src)/base/base.gyp:base',
        '<(src)/base/base.gyp:test_support_base',
        '<(src)/testing/gtest.gyp:gtest',
      ],
    },
  ],
}
