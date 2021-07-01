"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_playing = None
        self.is_video_playing = False
        self.videos_available = True
        self.video_paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        video_objects = self._video_library.get_all_videos()
        all_videos = []
        for video in video_objects:
            video_tags = " ".join(video.tags)
            video_info = f"{video.title} ({video.video_id}) [{video_tags}]"
            all_videos.append(video_info)
        all_videos = sorted(all_videos)
        #“title (video_id) [tags]”


        print("Here's a list of all available videos:")
        print(*all_videos, sep = "\n")
    
            
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        video_objects = self._video_library.get_all_videos()
        video_ids = []
        for video in video_objects:
            id = f"{video.video_id}"
            video_ids.append(id)

        if video_id not in video_ids:
            print("Cannot play video: Video does not exist")
            return

        if self.is_video_playing == False:
            self.video_playing = video_id
            self.is_video_playing = True
            print(f"Playing video: {self._video_library.get_video(self.video_playing).title}")
            return
    
        if self.is_video_playing == True:

            if video_id == self.video_playing:
                print(f"Stopping video: {self._video_library.get_video(self.video_playing).title}")
                print(f"Playing video: {self._video_library.get_video(video_id).title}")
                self.video_playing = video_id

            if video_id != self.video_playing:
                print(f"Stopping video: {self._video_library.get_video(self.video_playing).title}")
                print(f"Playing video: {self._video_library.get_video(video_id).title}")
                self.video_playing = video_id

        
    def stop_video(self):
        """Stops the current video."""

        if self.is_video_playing == False:
            print("Cannot stop video: No video is currently playing")

        if self.is_video_playing == True:
            print(f"Stopping video: {self._video_library.get_video(self.video_playing).title}")
            self.video_playing = None
            self.is_video_playing = False


    def play_random_video(self):
        """Plays a random video from the video library."""
        
        video_objects = self._video_library.get_all_videos()
        video_ids = []
        for video in video_objects:
            id = f"{video.video_id}"
            video_ids.append(id)

        self.play_video(random.choice(video_ids))
        
        if self.videos_available == False:
            print("No videos available")


    def pause_video(self):
        """Pauses the current video."""
        if self.is_video_playing == False:
            print("Cannot pause video: No video is currently playing")
            return
        if self.video_paused == True:
            print(f"Video already paused: {self._video_library.get_video(self.video_playing).title}")
        if self.video_paused == False:
            print(f"Pausing video: {self._video_library.get_video(self.video_playing).title}")
            self.video_paused = True
        

    def continue_video(self):
        """Resumes playing the current video."""

        if self.is_video_playing == False:
            print("Cannot continue video: No video is currently playing")
            return
        if self.video_paused == False:
            print("Cannot continue video: Video is not paused")
        if self.video_paused == True:
            print(f"Continuing video: {self._video_library.get_video(self.video_playing).title}")
            self.video_paused = False
        

    def show_playing(self):
        """Displays video currently playing."""
       
        if self.is_video_playing == True:
            video = self._video_library.get_video(self.video_playing)
            video_tags = " ".join(video.tags)
            video_info = f"{video.title} ({video.video_id}) [{video_tags}]"
            
            if self.video_paused == True:
                print(f"Currently playing: {video_info} - PAUSED")
            if self.video_paused == False:
                print(f"Currently playing: {video_info}")
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")

