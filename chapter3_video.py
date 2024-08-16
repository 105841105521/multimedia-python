from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import vfx

video = VideoFileClip('video.mp4')

short_video = video.subclip(0, 10) 
short_video.write_videofile('short_result.mp4')

combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile('combined_result.mp4')

reversed_video = short_video.fx(vfx.time_mirror)  
reversed_video.write_videofile('reversed_result.mp4')

sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile('SpeedUp_result.mp4')

video.write_videofile('result.mp4')