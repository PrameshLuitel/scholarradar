import { Img, AbsoluteFill, useCurrentFrame, interpolate, useVideoConfig } from 'remotion';

const images = [
    "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?q=80&w=1080&auto=format&fit=crop", // Graduation
    "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=1080&auto=format&fit=crop", // Airplane wing over clouds
    "https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?q=80&w=1080&auto=format&fit=crop", // University Library 
];

export const ImageCarousel: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  
  // Each image gets 60 frames (2 seconds)
  const imageIndex = Math.floor(frame / 60) % images.length;
  const progressInImage = frame % 60;
  
  // Slow zoom Ken Burns effect
  const scale = interpolate(progressInImage, [0, 60], [1.1, 1.25], { extrapolateRight: 'clamp' });
  const opacity = interpolate(progressInImage, [0, 10, 50, 60], [0, 1, 1, 0], { extrapolateRight: 'clamp' });

  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', backgroundColor: '#000' }}>
      <Img 
        src={images[imageIndex]} 
        style={{ 
            width: '100%', 
            height: '100%', 
            objectFit: 'cover',
            transform: `scale(${scale})`,
            opacity
        }} 
      />
      <AbsoluteFill style={{ justifyContent: 'flex-end', padding: 80, paddingBottom: 150 }}>
         {imageIndex === 0 && <h1 style={{ fontSize: 80, color: 'white', fontFamily: 'Inter', fontWeight: 800, textShadow: '0 4px 20px rgba(0,0,0,0.8)' }}>Discover Top Universities...</h1>}
         {imageIndex === 1 && <h1 style={{ fontSize: 80, color: 'white', fontFamily: 'Inter', fontWeight: 800, textShadow: '0 4px 20px rgba(0,0,0,0.8)' }}>Skip the Agency Fees...</h1>}
         {imageIndex === 2 && <h1 style={{ fontSize: 80, color: 'white', fontFamily: 'Inter', fontWeight: 800, textShadow: '0 4px 20px rgba(0,0,0,0.8)' }}>Your Future Starts Here.</h1>}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
