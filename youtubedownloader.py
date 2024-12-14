import os
import sys
import subprocess

try:
    from pytube import YouTube
    from moviepy.editor import VideoFileClip
except ImportError:
    print("Required libraries not found. Installing...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pytube', 'moviepy'])
    from pytube import YouTube
    from moviepy.editor import VideoFileClip

def check_ffmpeg():
    """Check if FFmpeg is installed and accessible"""
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        print("FFmpeg is not installed or not in system PATH.")
        print("Please download and install FFmpeg from: https://ffmpeg.org/download.html")
        print("Make sure to add FFmpeg to your system PATH.")
        return False

def download_youtube_video(url, output_path=None, format='mp4'):
    """
    Download a YouTube video in MP4 or MP3 format
    
    :param url: YouTube video URL
    :param output_path: Directory to save the file (uses current directory if not specified)
    :param format: Output format - 'mp4' or 'mp3'
    :return: Path to the downloaded file
    """
    try:
        # Set default output path to current directory if not specified
        if output_path is None:
            output_path = os.getcwd()
        
        # Ensure output directory exists
        os.makedirs(output_path, exist_ok=True)
        
        # Create YouTube object
        yt = YouTube(url)
        
        # Print video details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        print(f"Length: {yt.length} seconds")
        
        # Sanitize filename to remove invalid characters
        safe_title = "".join(c for c in yt.title if c.isalnum() or c in (' ', '.', '_')).rstrip()
        
        if format.lower() == 'mp4':
            # Get the highest resolution progressive stream
            video = yt.streams.get_highest_resolution()
            
            # Download the video
            print("Downloading MP4...")
            output_file = video.download(output_path, filename=f"{safe_title}.mp4")
            print(f"MP4 downloaded: {output_file}")
            return output_file
        
        elif format.lower() == 'mp3':
            # Check FFmpeg availability
            if not check_ffmpeg():
                return None
            
            # Download video first
            video = yt.streams.get_highest_resolution()
            temp_file = video.download(output_path)
            
            # Convert to MP3
            print("Converting to MP3...")
            video_clip = VideoFileClip(temp_file)
            audio_file = os.path.join(output_path, f"{safe_title}.mp3")
            video_clip.audio.write_audiofile(audio_file)
            
            # Close video clip and remove temporary video file
            video_clip.close()
            os.remove(temp_file)
            
            print(f"MP3 downloaded: {audio_file}")
            return audio_file
        
        else:
            raise ValueError("Format must be either 'mp4' or 'mp3'")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("YouTube Video Downloader")
    
    # Get YouTube URL from user
    url = input("Enter the YouTube video URL: ").strip()
    
    # Choose format
    while True:
        format = input("Choose format (mp4/mp3): ").lower()
        if format in ['mp4', 'mp3']:
            break
        print("Invalid format. Please choose mp4 or mp3.")
    
    # Optional: Specify output path
    output_path = input("Enter output directory (press Enter for current directory): ").strip()
    output_path = output_path if output_path else None
    
    # Download the video
    download_youtube_video(url, output_path, format)

if __name__ == "__main__":
    main()