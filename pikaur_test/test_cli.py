""" This file is licensed under GPLv3, see https://www.gnu.org/licenses/ """

from pikaur_test.helpers import PikaurTestCase, pikaur, pacman


class CliTest(PikaurTestCase):

    def test_unknown_argument(self):
        """
        unknown argument passed to pacman
        """
        self.assertEqual(pikaur('-Zyx').returncode, 1)

    def test_search(self):
        self.assertEqual(
            sorted(
                pikaur('-Ssq oomox').stdout.splitlines()
            ),
            ['oomox', 'oomox-git']
        )

    def test_aur_package_info(self):
        result = pikaur('-Si oomox')
        pkg_name_found = False
        for line in result.stdout.splitlines():
            if 'name' in line and 'oomox' in line:
                pkg_name_found = True
        self.assertTrue(pkg_name_found)

    def test_repo_package_info(self):
        result1 = pikaur('-Si mpv')
        result2 = pacman('-Si mpv')
        self.assertEqual(result1, result2)

    def test_incompatible_args(self):
        self.assertEqual(
            pikaur('-Qs pkg --repo').returncode, 1
        )
        self.assertEqual(
            pikaur('-Qs pkg --aur').returncode, 1
        )

    # just run info commands for coverage:

    def test_version(self):
        self.assertEqual(
            pikaur('-V').returncode, 0
        )

    def test_help(self):
        self.assertEqual(
            pikaur('-h').returncode, 0
        )

    def test_sync_help(self):
        self.assertEqual(
            pikaur('-Sh').returncode, 0
        )

    def test_query_help(self):
        self.assertEqual(
            pikaur('-Qh').returncode, 0
        )

    def test_pkgbuild_help(self):
        self.assertEqual(
            pikaur('-Ph').returncode, 0
        )

    def test_getpkgbuild_help(self):
        self.assertEqual(
            pikaur('-Gh').returncode, 0
        )
