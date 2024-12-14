import os
from pytube import YouTube
from pytube.exceptions import PytubeError, RegexMatchError
import requests

def download_video(link, format_choice):
    try:
        # Additional URL normalization
        if "youtu.be" in link:
            video_id = link.split("/")[-1].split("?")[0]
            link = f"https://www.youtube.com/watch?v={video_id}"
        
        # Try to verify the video link first
        try:
            response = requests.head(link, allow_redirects=True)
            if response.status_code != 200:
                print(f"Error: Unable to access the video. Status code: {response.status_code}")
                return
        except Exception as url_error:
            print(f"URL verification error: {url_error}")
            return

        # Create YouTube object
        yt = YouTube(link)
        
        # Additional title verification
        if not yt.title:
            print("Error: Unable to retrieve video title.")
            return

        print(f"Title: {yt.title}")
        print("Downloading...")
        
        if format_choice.lower() == "mp4":
            # Download video in highest resolution
            try:
                # Try multiple stream selection methods
                stream = (
                    yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution() or
                    yt.streams.filter(file_extension="mp4").get_highest_resolution() or
                    yt.streams.filter(file_extension="mp4").first()
                )
                
                if not stream:
                    print("No suitable video stream found.")
                    return

                # Sanitize filename to remove problematic characters
                safe_filename = "".join(c for c in yt.title if c.isalnum() or c in [' ', '-', '_']).rstrip()
                out_file = stream.download(output_path=os.getcwd(), filename=f"{safe_filename}.mp4")
                print(f"Video downloaded successfully: {os.path.basename(out_file)}")
            
            except Exception as stream_error:
                print(f"Error downloading video: {stream_error}")
        
        elif format_choice.lower() == "mp3":
            # Download only audio
            try:
                stream = yt.streams.filter(only_audio=True).first()
                
                if not stream:
                    print("No audio stream found.")
                    return

                # Sanitize filename
                safe_filename = "".join(c for c in yt.title if c.isalnum() or c in [' ', '-', '_']).rstrip()
                out_file = stream.download(output_path=os.getcwd(), filename=f"{safe_filename}_audio")
                
                # Convert to MP3
                base, _ = os.path.splitext(out_file)
                new_file = base + ".mp3"
                os.rename(out_file, new_file)
                
                print(f"Audio downloaded successfully: {os.path.basename(new_file)}")
            
            except Exception as audio_error:
                print(f"Error downloading audio: {audio_error}")
        
        else:
            print("Invalid format choice. Please choose either 'mp4' or 'mp3'.")
    
    except (PytubeError, RegexMatchError) as e:
        print(f"An error occurred while processing the YouTube link: {e}")
        print("Possible reasons:")
        print("- Invalid or restricted video")
        print("- Network issues")
        print("- Changes in YouTube's website structure")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the YouTube Downloader!")
    link = input("Paste the YouTube video link: ").strip()
    format_choice = input("Choose format to download (mp4/mp3): ").strip()
    download_video(link, format_choice)